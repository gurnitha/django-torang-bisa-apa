# apps/projects/forms.py

# Django modules
from django.forms import ModelForm

# Locals
from apps.projects.models import Project


# ProjectForm model
class ProjectForm(ModelForm):

	class Meta:
		model  = Project 
		fields = ['title', 'description', 'demo_link', 'source_link', 'tags']