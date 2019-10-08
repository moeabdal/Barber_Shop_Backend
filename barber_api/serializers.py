from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Barber, Service, Appointment
from datetime import datetime

def get_token(user):
		refresh = RefreshToken.for_user(user)
		return refresh.access_token

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	access = serializers.CharField(read_only=True)
	first_name = serializers.CharField(required=True)
	last_name = serializers.CharField(required=True)
	
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name', 'access',]
	
	def create(self, validated_data):
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username, first_name=first_name, last_name=last_name)
		new_user.set_password(password)
		new_user.save()
		validated_data["access"] = get_token(new_user)
		Barber.objects.create(user=new_user)
		return validated_data

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
	barber_name = serializers.SerializerMethodField()
	customer_name = serializers.SerializerMethodField()
	services = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

	class Meta:
		model = Appointment
		fields = ['id', 'barber_name', 'customer_name', 'date_and_time', 'available', 'services']

	def get_barber_name(self, obj):
		return obj.barber.user.first_name

	def get_customer_name(self, obj):
		if obj.user:
			return obj.user.user.first_name
		else:
			return ("")

class AppointmentCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields = ['date_and_time']


class BarberSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()
	future_appointments = serializers.SerializerMethodField()
	services = serializers.SerializerMethodField()
	past_appointments = serializers.SerializerMethodField()

	class Meta:
		model = Barber
		fields = ['user', 'name', 'image','nationality', 'telephone', 'credit', 'experience', 'services', 'future_appointments', 'past_appointments']

	def get_name(self, obj):
		return "%s %s"%(obj.user.first_name, obj.user.last_name)

	def get_future_appointments(self, obj):
		future_appointments = obj.barber_appointments.filter(date_and_time__gte=datetime.now())
		return AppointmentSerializer(future_appointments, many=True).data

	def get_past_appointments(self, obj):
		past_appointments = obj.barber_appointments.filter(date_and_time=datetime.now())
		return AppointmentSerializer(past_appointments, many=True).data

	def get_services(self, obj):
		services = obj.services.all()
		return ServiceSerializer(services, many=True).data

	


