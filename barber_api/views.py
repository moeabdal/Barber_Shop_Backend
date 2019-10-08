from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import UserCreateSerializer, BarberSerializer, ServiceSerializer, AppointmentSerializer, AppointmentCreateSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Barber, Service, Appointment
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsBarber


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class BarberListAPIView(ListAPIView):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer

class BarberProfileAPIView(RetrieveAPIView):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		user = self.request.user
		queryset = self.queryset.get(user=user)
		return queryset

class BarberUpdateAPIView(UpdateAPIView):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		user = self.request.user
		queryset = self.queryset.get(user=user)
		return queryset

class AppoinmentCreateAPIView(CreateAPIView):
	serializer_class = AppointmentCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(barber=self.request.user.barber)

class AppointmentDeleteAPIView(DestroyAPIView):
	queryset = Appointment.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'appointment_id'
	permission_classes = [IsAuthenticated, IsBarber]

class ServiceAPIView(ListAPIView):
	serializer_class = ServiceSerializer



