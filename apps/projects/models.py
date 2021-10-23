# apps/projects/models.py

# Django modules
from django.db import models
import uuid # to overide the default id in the table

# Locals
from apps.decors.models import Profile

# Create your models here.

# MODELS:Project
class Project(models.Model):
    owner = models.ForeignKey(
        Profile, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, # To keep the records eventhough he leaves
		help_text='Klik pilih owner. Field ini boleh dikosongkan.') 
    title = models.CharField(
        max_length=200,
        blank=False,
		help_text='Misal: Clone Twitter. Field ini tidak boleh dikosongkan.') 
    description = models.TextField(
        null=True, 
        blank=True,
		help_text='Field ini boleh dikosongkan.') 
    featured_image = models.ImageField(
    	upload_to='projects/',
        null=True, 
        blank=True, 
        default="projects/default.jpg")
    demo_link = models.CharField(
        max_length=2000, 
        null=True, 
        blank=True,
		help_text='Misal: https:www.demo.com Field ini boleh dikosongkan.') 
    source_link = models.CharField(
        max_length=2000, 
        null=True, 
        blank=True,
		help_text='Misal: https:www.demo.com Field ini boleh dikosongkan.') 
    tags = models.ManyToManyField(
        'Tag', # To put '' is not a must, but
               # it means Tag is resides bellow
        blank=True,
		help_text='Boleh pilih 1 atau lebih tags. Field ini boleh dikosongkan.') 
    vote_total = models.IntegerField(
        default=0, 
        null=True, 
        blank=True,
		help_text='Field ini boleh dikosongkan.') 
    vote_ratio = models.IntegerField(
        default=0, 
        null=True, 
        blank=True,
		help_text='Field ini boleh dikosongkan.') 
    created = models.DateTimeField(
		auto_now_add=True,
		help_text='Field untuk tanggal dibuat.') 
    updated = models.DateTimeField(
		auto_now=True,
		help_text='Field untuk tanggal diupdate.') 
    ''' Using uuid means that to overide 
        the default id in the table
        and use it as primary key and not editable'''
    id = models.UUIDField(
                default=uuid.uuid4, unique=True,
                primary_key=True, editable=False)

    def __str__(self):
        return self.title


# MODELS:Project
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey(
        Project,
        null=True, 
        blank=True, 
        on_delete=models.CASCADE,
		help_text='Klik pilih proyek. Field ini boleh dikosongkan.') 
    body = models.TextField(
        null=True, 
        blank=True,
		help_text='Field ini boleh dikosongkan.') 
    value = models.CharField(
        max_length=200,
        null=True, 
        blank=True,  
        choices=VOTE_TYPE,
		help_text='Klik pilih vote type. Field ini boleh dikosongkan.') 
    created = models.DateTimeField(
		auto_now_add=True,
		help_text='Field untuk tanggal dibuat.') 
    updated = models.DateTimeField(
		auto_now=True,
		help_text='Field untuk tanggal diupdate.') 
    ''' Using uuid means that to overide 
        the default id in the table
        and use it as primary key and not editable'''
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True,
        primary_key=True, 
        editable=False)

    def __str__(self):
        return self.value


# MODELS:Tag
class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        null=True, 
        blank=True,
		help_text='Misal: The City. Field ini boleh dikosongkan.') 
    created = models.DateTimeField(
		auto_now_add=True,
		help_text='Field untuk tanggal dibuat.') 
    updated = models.DateTimeField(
		auto_now=True,
		help_text='Field untuk tanggal diupdate.')
    ''' Using uuid means that to overide 
        the default id in the table
        and use it as primary key and not editable''' 
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True,
        primary_key=True, 
        editable=False)

    def __str__(self):
        return self.name