from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Service(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	description = models.TextField()
	duration = models.DurationField()

class Barber(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='barber_profile')
	image = models.ImageField(blank=True, null=True)
	experience = models.IntegerField(default=0)
	services = models.ManyToManyField(Service)
	nationality = models.CharField(max_length=100)
	credit = models.IntegerField(default=0)




