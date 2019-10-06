from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'access']

    def create(self, validated_data):
        first_name = validated_data['first_name']
		last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
		validated_data["access"] = get_token(new_user)
        return validated_data

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['user', 'image', 'credit', 'telephone', 'address']

		