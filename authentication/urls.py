from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='registration'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
]
