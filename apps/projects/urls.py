# apps/projects/urls.py

# Django modules
from django.urls import path

# Locals
from apps.projects import views

# Appname
app_name = 'projects'

urlpatterns = [
	path('projects/', views.project_list, name='project_list'),
	path('project-detail/<str:pk>/', views.project_detail, name='project_detail')
]