# apps/profiles/urls.py

# Django modules
from django.urls import path

# Locals
from apps.profiles import views

# Appname
app_name = 'profiles'

urlpatterns = [
	path('', views.profile_list, name='profile_list'),
	path('profile-detail/<str:pk>/', views.profile_detail, name='profile_detail')
]