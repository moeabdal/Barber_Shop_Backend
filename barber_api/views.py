from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, BarberSerializer, ServiceSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Barber, Service


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class BarberAPIView(ModelViewSet):
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

	# override get queryset to filter by Barber


