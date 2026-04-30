from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Lifestyle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    sleep_hours = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    exercise_hours = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    diet_quality = models.CharField(
        max_length=20,
        choices=[
            ('poor', 'Poor'),
            ('fair', 'Fair'),
            ('good', 'Good'),
            ('excellent', 'Excellent'),
        ],
        default='good',
    )
    lifestyle_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lifestyle for {self.user} ({self.created_at:%Y-%m-%d})"
    
    class Meta:
        ordering = ['-created_at']
