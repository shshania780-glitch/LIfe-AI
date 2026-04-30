from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import sys
import os

# Add parent directory to path to import app.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from app import predict_lifestyle_score

from .forms import LifestyleForm
from .models import Lifestyle

@login_required(login_url='login')
def lifestyle_form(request):
    prediction_result = None
    submitted_data = None
    
    if request.method == 'POST':
        form = LifestyleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            
            # Calculate prediction score
            try:
                score = predict_lifestyle_score(
                    sleep_hours=obj.sleep_hours,
                    exercise_hours=obj.exercise_hours,
                    diet_quality=obj.diet_quality
                )
                obj.lifestyle_score = score
                prediction_result = {
                    'score': score,
                    'sleep_hours': obj.sleep_hours,
                    'exercise_hours': obj.exercise_hours,
                    'diet_quality': obj.get_diet_quality_display(),
                    'address': obj.address
                }
                submitted_data = obj
            except Exception as e:
                print(f"Prediction error: {e}")
                obj.lifestyle_score = 0
            
            obj.save()
            # Don't redirect - show result on same page
            # return redirect('profile')
    else:
        form = LifestyleForm()

    return render(request, 'lifestyle_form.html', {
        'form': form,
        'prediction_result': prediction_result,
        'submitted_data': submitted_data
    })

@login_required(login_url='login')
def prediction_result(request, id):
    """Display prediction result for a lifestyle entry"""
    lifestyle = get_object_or_404(Lifestyle, id=id, user=request.user)
    
    return render(request, 'prediction_result.html', {
        'lifestyle': lifestyle,
        'score': lifestyle.lifestyle_score
    })

@login_required(login_url='login')
def delete_lifestyle(request, id):
    """Delete a lifestyle entry"""
    lifestyle = get_object_or_404(Lifestyle, id=id, user=request.user)
    if request.method == 'POST':
        lifestyle.delete()
        return redirect('profile')
    return redirect('profile')