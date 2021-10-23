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
		help_text='Klik pilih user. Field ini boleh dikosongkan.') 
    name = models.CharField(
		max_length=50,
		blank=False,
		null=False,
		help_text='Misal: Bisma. Field ini tidak boleh dikosongkan.') 
    email = models.EmailField(
    	max_length=500, 
    	blank=True, 
    	null=True,
		help_text='Misal: bisma@gmail.com. Field ini boleh dikosongkan.') 
    username = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Misal: Kakek Bisma. Field ini boleh dikosongkan.') 
    location = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Misal: New Delhi, India. Field ini boleh dikosongkan.') 
    short_intro = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Keterangan ringkas ttg Anda. Field ini boleh dikosongkan.') 
    bio = models.TextField(
    	blank=True, 
    	null=True,
		help_text='Field ini boleh dikosongkan.') 
    profile_image = models.ImageField(
		upload_to='profiles/',
		default='profiles/user-default.png',
		blank=True,
		null=True,
		help_text='Misal foto Anda. Field ini boleh dikosongkan.') 
    facebook = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Account Anda di FB. Field ini boleh dikosongkan.')  
    twitter = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Account Anda di Twt. Field ini boleh dikosongkan.') 
    instagram= models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Account Anda di IG. Field ini boleh dikosongkan.') 
    linkedin= models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Account Anda di Linkedin. Field ini boleh dikosongkan.') 
    youtube= models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Account Anda di Ytb. Field ini boleh dikosongkan.') 
    stackoverflow = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Account Anda di Stackoverflow. Field ini boleh dikosongkan.')
    github = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Account Anda di Github. Field ini boleh dikosongkan.')
    website = models.CharField(
    	max_length=200, 
    	blank=True, 
    	null=True,
		help_text='Misal: https://www.bisma.com Field ini boleh dikosongkan.') 
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
		help_text='Klik pilih owner. Field ini boleh dikosongkan.') 
    skill = models.CharField(
		max_length=50,
		blank=False,
		null=False,
		help_text='Misal: PHP. Field ini boleh dikosongkan.')
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