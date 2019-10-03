from django.db import models
from django import forms
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
	image = models.ImageField(blank=True, null=True)
	telephone = models.IntegerField(default=0, min_length=9)
	address = models.CharField(max_length=100)
	credit = models.IntegerField(default=0)


