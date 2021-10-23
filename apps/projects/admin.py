# apps/projects/admin.py

# Django modules
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Locals
from apps.projects.models import Project, Review, Tag


# ---------CKEditor untuk Project model -----------------

# Project admin form for CKEditor
class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(required=False,widget=CKEditorUploadingWidget)

    class Meta:
      model  = Project 
      fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    form = ProjectAdminForm

admin.site.register(Project, ProjectAdmin)

# ---------END CKEditor untuk Project model ------------

# ---------CKEditor untuk Review model -----------------
# Project admin form for CKEditor
class ReviewAdminForm(forms.ModelForm):
    body = forms.CharField(required=False,widget=CKEditorUploadingWidget)

    class Meta:
      model  = Review 
      fields = '__all__'

class ReviewAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    form = ReviewAdminForm

admin.site.register(Review, ReviewAdmin)
# ---------END CKEditor untuk Review model ------------

admin.site.register(Tag)

