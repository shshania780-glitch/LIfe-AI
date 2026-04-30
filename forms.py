from django import forms
from .models import Lifestyle

class LifestyleForm(forms.ModelForm):
    class Meta:
        model = Lifestyle
        fields = [
            'address',
            'sleep_hours',
            'exercise_hours',
            'diet_quality'
        ]
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'sleep_hours': forms.NumberInput(attrs={'placeholder': 'Hours', 'step': '0.1'}),
            'exercise_hours': forms.NumberInput(attrs={'placeholder': 'Hours', 'step': '0.1'}),
        }