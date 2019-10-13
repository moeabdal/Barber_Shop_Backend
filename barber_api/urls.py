"""BarberShop_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static


urlpatterns = [
	path('register/', UserCreateAPIView.as_view(), name='register'),
	path('list/', BarberListAPIView.as_view(), name='barber-list'),
	path('profile/', BarberProfileAPIView.as_view(), name='barber-profile'),
	path('profile/update/', BarberUpdateAPIView.as_view(), name='barber-update'),
	path('appointment/create/', AppoinmentCreateAPIView.as_view(), name='appointments'),
	path('appointment/delete/<int:appointment_id>/', AppointmentDeleteAPIView.as_view(), name='apppointment-delete'),
	path('appointment/update/<int:appointment_id>/', BarberAppointmentUpdateAPIView.as_view(), name='apppointment-update')
	# path(r'^ratings/', include('star_ratings.urls', namespace='ratings', barber_api='ratings')).
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)