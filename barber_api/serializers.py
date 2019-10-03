from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Barber, Service, Appointment

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
		return validated_data

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		exclude ='__all__'

class BarberSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()
	class Meta:
		model = Barber
		fields = ['user', 'name', 'image', 'credit', 'experience', 'services', 'appointments']

	def get_name(self, obj):
		return "%s %s"%(obj.user.first_name, obj.user.last_name)

	


