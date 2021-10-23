# Generated by Django 3.2.5 on 2021-10-23 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(help_text='Field ini tidak boleh dikosongkan.', max_length=50)),
                ('email', models.EmailField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=500, null=True)),
                ('username', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('location', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('short_intro', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('bio', models.TextField(blank=True, help_text='Field ini boleh dikosongkan.', null=True)),
                ('profile_image', models.ImageField(blank=True, default='profiles/user-default.png', help_text='Field ini boleh dikosongkan.', null=True, upload_to='profiles/')),
                ('facebook', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('telegram', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('inkedin', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('youtube', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('stackoverflow', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('website', models.CharField(blank=True, help_text='Field ini boleh dikosongkan.', max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Field untuk tanggal dibuat.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Field untuk tanggal diupdate.')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='User id', primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, help_text='Field ini boleh dikosongkan.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill', models.CharField(help_text='Field ini boleh dikosongkan.', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Field untuk tanggal dibuat.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Field untuk tanggal diupdate.')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='User id', primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, help_text='Field ini boleh dikosongkan.', null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]