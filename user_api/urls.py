
from django.urls import path, include

from .views import *


urlpatterns = [
	path('register/', UserCreateAPIView.as_view(), name='register'),
	path('profile/', ProfileAPIView.as_view(), name='user-profile'),
	path('profile/update/', ProfileUpdateAPIView.as_view(), name='user-profile-update'),
	path('appointment/update/<int:appointment_id>/', AppointmentUpdateAPIView.as_view(), name='user-appointment-update'),
]

