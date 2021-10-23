# apps/profiles/views.py

# Django modules
from django.shortcuts import render

# Locals

# profile_list view
def profile_list(request):
	page_title = 'Profile List'
	context = {
		'title':page_title,
	}
	return render(request, 'profiles/profile_list.html', context)


# profile_detail view
def profile_detail(request):
	page_title = 'Profile Detail'
	context = {
		'title':page_title,
	}
	return render(request, 'profiles/profile_detail.html', context)