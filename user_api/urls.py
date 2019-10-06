
from django.urls import path, include

from .views import *


urlpatterns = [
	path('userregister/', UserCreateAPIView.as_view(), name='user_register')]