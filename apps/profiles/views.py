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
def profile_detail(request, pk):
	
	# Page title
	page_title = 'Profile Detail'
	
	# Profile by id
	profile = Profile.objects.get(id=pk)
	
	# Skill yg memiliki deskripsi
	topSkills = profile.skill_set.exclude(description__exact="")
	
	# Skill yg tidak memiliki deskripsi
	otherSkills = profile.skill_set.filter(description__exact="")

	context = {
		'title':page_title,
		'profile':profile,
		'topSkills':topSkills,
		'otherSkills':otherSkills
	}
	return render(request, 'profiles/profile_detail.html', context)