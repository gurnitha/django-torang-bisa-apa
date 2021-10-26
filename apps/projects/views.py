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


# create_project view
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