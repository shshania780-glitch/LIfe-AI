from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import LoginForm

@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            return render(request, 'registration/register.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('form')
    
    return render(request, 'registration/register.html')

@require_http_methods(["GET", "POST"])
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('form')
            else:
                form.add_error(None, 'Invalid credentials')
                return render(request, 'registration/login.html', {'form': form})
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    from predictions.models import Lifestyle
    from django.db.models import Avg
    
    lifestyle_data = Lifestyle.objects.filter(user=request.user).order_by('-created_at')
    
    # Calculate averages
    stats = lifestyle_data.aggregate(
        avg_sleep=Avg('sleep_hours'),
        avg_exercise=Avg('exercise_hours')
    )
    
    latest_sleep = round(stats['avg_sleep'], 1) if stats['avg_sleep'] else None
    latest_exercise = round(stats['avg_exercise'], 1) if stats['avg_exercise'] else None
    
    return render(request, 'registration/profile.html', {
        'lifestyle_data': lifestyle_data,
        'latest_sleep': latest_sleep,
        'latest_exercise': latest_exercise
    })
