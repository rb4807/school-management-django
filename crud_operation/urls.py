from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('data/', views.data, name='data'),
    path('create/', views.create, name='create'),
    path('update/<int:member_id>/', views.update, name='update'),
    path('delete/<int:member_id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),


]
