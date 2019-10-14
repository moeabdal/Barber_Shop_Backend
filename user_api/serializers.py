from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from barber_api.models import Appointment, Service
from barber_api.serializers import AppointmentSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime
from django.db.models import Sum

def get_token(user):
		refresh = RefreshToken.for_user(user)
		return refresh.access_token

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	access = serializers.CharField(read_only=True)
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name', 'access']

	def create(self, validated_data):
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		username = validated_data['username']
		password = validated_data['password']

		new_user = User(username=username, first_name= first_name, last_name=last_name)

		new_user.set_password(password)
		new_user.save()
		validated_data["access"] = get_token(new_user)
		Profile.objects.create(user=new_user)
		return validated_data

class ProfileSerializer(serializers.ModelSerializer):
	name = serializers.SerializerMethodField()
	future_appointments = serializers.SerializerMethodField()
	past_appointments = serializers.SerializerMethodField()
	class Meta:
		model = Profile
		fields = ['name', 'image', 'telephone', 'address', 'future_appointments', 'past_appointments']

	def get_name(self, obj):
		return "%s %s"%(obj.user.first_name, obj.user.last_name)

	def get_future_appointments(self, obj):
		appointments = obj.user_appointments.filter(date_and_time__gte=datetime.now())
		return AppointmentSerializer(appointments, many=True).data

	def get_past_appointments(self, obj):
		appointments = obj.user_appointments.filter(date_and_time__lte=datetime.now())
		return AppointmentSerializer(appointments, many=True).data

class ProfileUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['image', 'telephone', 'address']

class AppointmentUpdateSerializer(serializers.ModelSerializer):
	services = serializers.PrimaryKeyRelatedField(many=True, queryset=Service.objects.all())
	total_price = serializers.SerializerMethodField()
	total_duration_minutes = serializers.SerializerMethodField()
	class Meta:
		model = Appointment
		fields = ['services', 'total_price', 'total_duration_minutes']

	def get_total_price(self, obj):
		return obj.total_price()

	def get_total_duration_minutes(self, obj):
		total = obj.services.aggregate(Sum('duration'))
		total_minutes = total.get('duration__sum')/60
		return total_minutes



