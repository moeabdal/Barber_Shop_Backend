from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import UserCreateSerializer, ProfileSerializer, ProfileUpdateSerializer, AppointmentUpdateSerializer
from .models import Profile
from barber_api.models import Appointment
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.db.models import Sum

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProfileAPIView(RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		user = self.request.user
		queryset = self.queryset.get(user=user)
		return queryset

class ProfileUpdateAPIView(UpdateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileUpdateSerializer
	permission_classes = [IsAuthenticated]


	def get_object(self):
		user = self.request.user
		queryset = self.queryset.get(user=user)
		return queryset

class AppointmentUpdateAPIView(UpdateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'appointment_id'
	permission_classes = [IsAuthenticated]

	def perform_update(self, serializer):
		if self.get_object().user and self.request.data.get('services') == None:
			serializer.save(user=None, available=True)
		else:
			total_price = Appointment.objects.annotate(total_price=Sum('services__price'))
			print (total_price)
			# print (self.get_object().user.credit)
			serializer.save(user=self.request.user.user_profile)