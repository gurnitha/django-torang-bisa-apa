# apps/projects/views.py

# Django modules
from django.shortcuts import render

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


# # project_detail view
# def project_detail(request):
# 	page_title = 'Project Detail'
# 	context = {
# 		'title':page_title
# 	}
# 	return render(request, 'projects/project_detail.html', context)


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