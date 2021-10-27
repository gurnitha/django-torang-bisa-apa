# apps/decors/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.decors.models import Profile
from apps.decors.forms import SkillForm

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
	return render(request, 'decors/profile_list.html', context)


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
	return render(request, 'decors/profile_detail.html', context)




# ----------------------CRUD SKILLS BASICS----------------------


# create_skill view (tampa autentikasi)
# 1. Membuat create_skill view method
def create_skill(request):

	# 2. Gunakan SkillForm model
	form = SkillForm()


	# Context dictionary
	context = {
		'form':form,
	} 

	# Template
	return render(request, 'decors/crud/create_skill.html', context)

# ----------------------END CRUD SKILLS BASICS------------------
