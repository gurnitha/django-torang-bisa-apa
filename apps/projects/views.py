# apps/projects/views.py

# Django modules
from django.shortcuts import render

# Locals


# project_list view
def project_list(request):
	page_title = 'Project List'
	context = {
		'title':page_title
	}
	return render(request, 'projects/project_list.html', context)


# project_detail view
def project_detail(request):
	page_title = 'Project Detail'
	context = {
		'title':page_title
	}
	return render(request, 'projects/project_detail.html', context)