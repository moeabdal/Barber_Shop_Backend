from django.db import models
from django import forms
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
	image = models.ImageField(blank=True, null=True)
	telephone = models.IntegerField(default=0)
	address = models.CharField(max_length=100)
	credit = models.IntegerField(default=0)


