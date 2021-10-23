# apps/profiles/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import User
import uuid

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		help_text='Field ini boleh dikosongkan.') 
    name = models.CharField(
		max_length=50,
		blank=False,
		null=False,
		help_text='Field ini tidak boleh dikosongkan.') 
    email = models.EmailField(
    	max_length=500, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    username = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    location = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    short_intro = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    bio = models.TextField(
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    profile_image = models.ImageField(
		upload_to='profiles/',
		default='profiles/user-default.png',
		blank=True,
		null=True,
		help_text='Field ini boleh dikosongkan.') 
    facebook = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.')  
    twitter = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    instagram= models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    telegram= models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.')
    inkedin= models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    youtube= models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    stackoverflow = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.')
    website = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    created = models.DateTimeField(
		auto_now_add=True,
		help_text='Field untuk tanggal dibuat.') 
    updated = models.DateTimeField(
		auto_now=True,
		help_text='Field untuk tanggal diupdate.') 
    id = models.UUIDField(
    	default=uuid.uuid4, 
    	unique=True,
    	primary_key=True, 
    	editable=False,
		help_text='User id') 

    def __str__(self):
    	return self.name


# Skill model
class Skill(models.Model):
    owner = models.ForeignKey(
		Profile,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		help_text='Field ini boleh dikosongkan.') 
    skill = models.CharField(
		max_length=50,
		blank=False,
		null=False,
		help_text='Field ini boleh dikosongkan.')
    created = models.DateTimeField(
		auto_now_add=True,
		help_text='Field untuk tanggal dibuat.') 
    updated = models.DateTimeField(
		auto_now=True,
		help_text='Field untuk tanggal diupdate.') 
    id = models.UUIDField(
    	default=uuid.uuid4, 
    	unique=True,
    	primary_key=True, 
    	editable=False,
		help_text='User id') 

    def __str__(self):
    	return self.skill