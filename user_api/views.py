from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import UserCreateSerializer, ProfileSerilizer
from .models import Profile

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProfileAPIView(ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'profile_id'