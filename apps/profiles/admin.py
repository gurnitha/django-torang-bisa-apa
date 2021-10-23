# apps/profiles/admin.py

# Django modules
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Locals
from apps.profiles.models import Profile, Skill

# Register your model here


# Post admin form for CKEditor
class ProfileAdminForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
      model  = Profile 
      fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    form = ProfileAdminForm

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill)