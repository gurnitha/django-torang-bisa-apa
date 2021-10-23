# apps/projects/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.projects.models import Project, Review, Tag

# Register your model here

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

