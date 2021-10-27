
# decors/forms.py

# Django modules
from django.forms import ModelForm, widgets
from django import forms

# Locals
from .models import Skill

# Create your forms here.

# Naming the class: ModelName+Form
class SkillForm(ModelForm):
	class Meta:
		model = Skill
		fields = '__all__'
		exclude = ['owner']

		# Change multiple select to multiple radion button
		widgets = {'tags': forms.CheckboxSelectMultiple(),}

	def __init__(self, *args, **kwargs):
		super(SkillForm, self).__init__(*args, **kwargs)

 		# REPLACING THE BELOW TECHNIQUE USING FOR LOOP
		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'input'})
	
