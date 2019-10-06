from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from .serializers import UserCreateSerializer, ProfileSerializer
from .models import Profile

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProfileAPIView(RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'profile_id'

	def get_object(self):
		user = self.request.user
		queryset = self.queryset.get(user=user)
		return queryset