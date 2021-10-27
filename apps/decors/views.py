# apps/decors/views.py

# Django modules
from django.shortcuts import render, redirect

# Locals
from apps.decors.models import Profile, Skill
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

	# 3. Proses the form kalau request method adalah POST
	#    dan jalankan SkillForm model
	if request.method == "POST":

		# # Tesing the form (opsional): fillin the form and submit it
		# print(request.POST) # tested :)

		form = SkillForm(request.POST)

		# 4. Validasi form dan jika valid,
		#    simpan skill
		if form.is_valid():
			form.save()

			# 5. Arahkan user ke halaman account
			return redirect('decors:profile_list')

	# Context dictionary
	context = {
		'form':form,
	} 

	# Template
	return render(request, 'decors/crud/create_skill.html', context)



# update_skill view (tampa autentikasi)
# 1. Tambahkan parameter pk pada update_skill view method
def update_skill(request, pk):

	# 2. Dapatkan id proyek yang akan diupdate
	skill = Skill.objects.get(id=pk)

	# 3. Masukan instan skill object ke dalam form
	form = SkillForm(instance=skill)

	# 4. Proses form jika metode requestnya adalah POST
	if request.method == 'POST':

		# Testing (opsional)
		# print(request.POST)

		form = SkillForm(request.POST, instance=skill)

		# 5. Simpan proyek, jika form valid
		if form.is_valid():
			form.save()

			# 6. Stlh proyek berhasil di simpan
			#    Arahkan user ke halaman profile_list
			return redirect('decors:profile_list')

	# Context dictinary
	context = {'form':form}

	# Template
	return render(request, 'decors/crud/create_skill.html', context)



# delete_skill view (tampa autentikasi)
# 1. Tambahkan parameter pk pada delete_skill view method
def delete_skill(request, pk):

	# 2. Dapatkan id skill yang akan didelete
	skill = Skill.objects.get(id=pk)

	# 3. Proses form jika metode requestnya adalah POST
	#    dan gunakan delete method untuk menghapus skill
	if request.method == 'POST':

		skill.delete()

		# 4. Stlh skill berhasil dihapus,
		#    arahkan user ke halaman skill_list
		return redirect('decors:profile_list')

	# Context dictinary
	context = {'object':skill}

	# Template
	return render(request, 'decors/crud/delete_template.html', context)
# ----------------------END CRUD SKILLS BASICS------------------
