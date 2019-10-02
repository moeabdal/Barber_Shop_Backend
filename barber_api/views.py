from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer, ProfileSerializer, ServiceSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Profile, Service


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProfileAPIView(ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'profile_id'

class ServiceAPIView(ModelViewSet):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'service_id'

