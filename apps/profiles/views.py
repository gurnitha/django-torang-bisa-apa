# apps/profiles/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.profiles.models import Profile, Skill


# profile_list view
def profile_list(request):
	page_title = 'Profile List'
	profiles = Profile.objects.all()
	skills = Skill.objects.all()
	context = {
		'title':page_title,
		'profiles':profiles,
		'skills':skills
	}
	return render(request, 'profiles/profile_list.html', context)


# profile_detail view
def profile_detail(request):
	page_title = 'Profile Detail'
	context = {
		'title':page_title,
	}
	return render(request, 'profiles/profile_detail.html', context)