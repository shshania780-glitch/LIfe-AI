from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from predictions.views import lifestyle_form, prediction_result, delete_lifestyle
from users.views import register, user_login, user_logout, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/', permanent=False), name='home'),
    path('form/', lifestyle_form, name='form'),
    path('prediction/<int:id>/', prediction_result, name='prediction'),
    path('delete/<int:id>/', delete_lifestyle, name='delete_lifestyle'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('accounts/profile/', RedirectView.as_view(url='/profile/', permanent=False)),

    # 👇 Django built-in login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]