from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from .serializers import UserCreateSerializer, BarberSerializer, ServiceSerializer, AppointmentSerializer, AppointmentCreateSerializer, BarberAppointmentUpdateSerializer, BarberProfileSerializer, TokenObtainPairSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Barber, Service, Appointment
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsBarber
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class BarberListAPIView(ListAPIView):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer

class BarberProfileAPIView(RetrieveAPIView):
	queryset = Barber.objects.all()
	serializer_class = BarberProfileSerializer
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

class BarberAppointmentUpdateAPIView(UpdateAPIView):
	queryset = Appointment.objects.all()
	serializer_class = BarberAppointmentUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'appointment_id'
	# permission_classes = [IsAuthenticated, IsBarber]

	def perform_update(self, serializer):
		if self.get_object().barber:
			new_barber_credit = self.get_object().barber.credit = (self.get_object().barber.credit + self.get_object().total_price())
			barber = self.get_object().barber
			barber.credit = new_barber_credit
			barber.save()
			new_credit = self.get_object().user.credit = (self.get_object().user.credit - self.get_object().total_price())
			user = self.get_object().user
			user.credit = new_credit
			user.save()
			print (self.get_object().barber.credit)


class TokenObtainPairView(APIView):
	def post(self, request):
		auth_user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
		print (request.data)
		if auth_user is not None:
			refresh = RefreshToken.for_user(auth_user)
			if Barber.objects.filter(user=auth_user):
				is_barber = True
			else:
				is_barber = False
			return Response({
							'refresh': str(refresh),
							'access': str(refresh.access_token),
							'barber': is_barber
						})





