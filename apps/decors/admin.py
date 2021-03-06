# apps/decors/admin.py

# Django modules
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Locals
from apps.decors.models import Profile, Skill



# Profile admin form for CKEditor
class ProfileAdminForm(forms.ModelForm):
    bio = forms.CharField(required=False,widget=CKEditorUploadingWidget)

    class Meta:
      model  = Profile 
      fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    form = ProfileAdminForm


# Skill admin form for CKEditor
class SkillAdminForm(forms.ModelForm):
    description = forms.CharField(required=False,widget=CKEditorUploadingWidget)

    class Meta:
      model  = Skill 
      fields = '__all__'


class SkillAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    form = SkillAdminForm

# Register your model here

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)