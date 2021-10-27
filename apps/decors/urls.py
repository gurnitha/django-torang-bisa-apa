# apps/decors/urls.py

# Django modules
from django.urls import path

# Locals
from apps.decors import views

# Appname
app_name = 'decors'

urlpatterns = [

	# SKILLS CRUD
	path('create-skill/', views.create_skill, name='create_skill'),
	path('update-skill/<str:pk>/', views.update_skill, name='update_skill'),
	path('', views.profile_list, name='profile_list'),
	path('profile-detail/<str:pk>/', views.profile_detail, name='profile_detail')
]