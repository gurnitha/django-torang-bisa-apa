# apps/projects/views.py

# Django modules
from django.shortcuts import render, redirect
from apps.projects.forms import ProjectForm

# Locals
from apps.projects.models import Project, Tag


# project_list view
def project_list(request):
	tags = Tag.objects.all()
	projects = Project.objects.all()
	page_title = 'Project List'
	context = {
		'tags':tags,
		'projects':projects,
		'title':page_title
	}
	return render(request, 'projects/project_list.html', context)


# project_detail view
def project_detail(request, pk):
	
	# Page title
	page_title = 'Project Detail'
	
	# project by id
	project = Project.objects.get(id=pk)
	

	context = {
		'title':page_title,
		'project':project,
	}
	return render(request, 'projects/project_detail.html', context)


# ----------------------CRUD PROJECTS BASICS----------------------

# create_project view (tampa autentikasi)
def create_project(request):

	# Bring in the ProjectForm class
	form = ProjectForm()

	# If there is POST request, process the form
	if request.method == "POST":

		# Tesing the form: fillin the form and submit it
		# print(request.POST) # tested :)

		# Instantiate the ProjectForm class
		form = ProjectForm(request.POST)
		# Check if form input is valid
		if form.is_valid():
			# Save the input
			form.save()
			return redirect('projects:project_list')

	# Context dictionary
	context = {
		'form':form,
	} 

	# Template
	return render(request, 'projects/crud/create_project.html', context)



# update_project view (tampa autentikasi)
# 1. Tambahkan parameter pk pada update_project view method
def update_project(request, pk):

	# 2. Dapatkan id proyek yang akan diupdate
	project = Project.objects.get(id=pk)

	# 3. Masukan instan project object ke dalam form
	form = ProjectForm(instance=project)

	# 4. Proses form jika metode requestnya adalah POST
	if request.method == 'POST':

		# Testing (opsional)
		# print(request.POST)

		form = ProjectForm(request.POST, instance=project)

		# 5. Simpan proyek, jika form valid
		if form.is_valid():
			form.save()

			# 6. Stlh proyek berhasil di simpan
			#    Arahkan user ke halaman project_list
			return redirect('projects:project_list')

	# Context dictinary
	context = {'form':form}

	# Template
	return render(request, 'projects/crud/create_project.html', context)



# delete_project view (tampa autentikasi)
# 1. Tambahkan parameter pk pada update_project view method
def delete_project(request, pk):

	# 2. Dapatkan id proyek yang akan diupdate
	project = Project.objects.get(id=pk)

	# 3. Proses form jika metode requestnya adalah POST
	#    dan gunakan delete method untuk menghapus proyek
	if request.method == 'POST':

		project.delete()

		# 4. Stlh proyek berhasil dihapus,
		#    arahkan user ke halaman project_list
		return redirect('projects:project_list')

	# Context dictinary
	context = {'object':project}

	# Template
	return render(request, 'projects/crud/delete_template.html', context)
# ----------------------END CRUD PROJECTS BASICS------------------
