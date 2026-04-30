from django.contrib import admin
from .models import Lifestyle

@admin.register(Lifestyle)
class LifestyleAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'sleep_hours', 'exercise_hours', 'diet_quality', 'created_at')
    list_filter = ('diet_quality', 'created_at')
    search_fields = ('user__username', 'address')
    readonly_fields = ('created_at',)
