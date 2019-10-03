from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Service(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	description = models.TextField()
	duration = models.DurationField()

	def __str__(self):
		return self.name

class Appointment(models.Model):
	barber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_appointments')
	appointment = models.DateTimeField()
	available = models.BooleanField(default=True)

	def __str__(self):
		return "%s Appointment"%(self.barber.first_name)

class Barber(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='barber')
	image = models.ImageField(blank=True, null=True)
	experience = models.IntegerField(default=0)
	services = models.ManyToManyField(Service, related_name='barber_services')
	nationality = models.CharField(max_length=100)
	credit = models.IntegerField(default=0)
	appointments = models.ManyToManyField(Appointment, related_name='barber_appointments')

	def __str__(self):
		return self.user.first_name




@receiver(post_save, sender=User)
def create_barber(instance, created, **kwargs):
	if created:
		Barber.objects.create(user=instance)



