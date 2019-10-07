from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import UserCreateSerializer, ProfileSerializer, ProfileUpdateSerializer, AppointmentUpdateSerializer
from .models import Profile
from barber_api.models import Appointment

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProfileAPIView(RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

	def get_object(self):
		user = self.request.user
		queryset = self.queryset.get(user=user)
		return queryset

class ProfileUpdateAPIView(UpdateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileUpdateSerializer

	def get_object(self):
		user = self.request.user
		queryset = self.queryset.get(user=user)
		return queryset

class AppointmentUpdateAPIView(UpdateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'appointment_id'

	def perform_update(self, serializer):
		if self.get_object().user:
			serializer.save(user=None, available=True)
		else:
			serializer.save(user=self.request.user.user_profile)