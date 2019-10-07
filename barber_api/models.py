from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from user_api.models import Profile

class Service(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	description = models.TextField()
	duration = models.DurationField()

	def __str__(self):
		return self.name

class Barber(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='barber')
	image = models.ImageField(blank=True, null=True)
	experience = models.IntegerField(default=0)
	telephone = models.IntegerField(default=0)
	services = models.ManyToManyField(Service, related_name='barbers')
	nationality = models.CharField(max_length=100)
	credit = models.IntegerField(default=0)


	def __str__(self):
		return self.user.first_name


class Appointment(models.Model):
	barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='barber_appointments')
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_appointments', null=True, blank=True)
	appointment = models.DateTimeField()
	available = models.BooleanField(default=True)
	services = models.ManyToManyField(Service)

	def __str__(self):
		return "%s %s's Appointment (%s)"%(self.barber.user.first_name, self.barber.user.last_name, self.id)