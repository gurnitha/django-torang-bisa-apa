# apps/decors/urls.py

# Django modules
from django.urls import path

# Locals
from apps.decors import views

# Appname
app_name = 'decors'

urlpatterns = [
	path('', views.profile_list, name='profile_list'),
	path('profile-detail/<str:pk>/', views.profile_detail, name='profile_detail')
]