from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .serializers import UserCreateSerializer, BarberSerializer, ServiceSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Barber, Service


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class BarberListAPIView(ListAPIView):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer

class BarberDetailAPIView(RetrieveAPIView):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'barber_id'

	def get_queryset(self):
		user = self.request.user
		queryset = self.queryset.filter(user=user)
		return queryset

class BarberUpdateAPIView(UpdateAPIView):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'barber_id'

	def get_queryset(self):
		user = self.request.user
		queryset = self.queryset.filter(user=user)
		return queryset


class ServiceAPIView(ListAPIView):
	serializer_class = ServiceSerializer



