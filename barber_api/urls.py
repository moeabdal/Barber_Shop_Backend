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
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("barber", BarberProfileAPIView)


urlpatterns = [
	path('register/', UserCreateAPIView.as_view(), name='register'),
	path('login/', TokenObtainPairView.as_view() , name='login'),
	path('barber/list/', BarberListAPIView.as_view(), name='barber-list'),
	path('barber/detail/<int:barber_id>', BarberDetailAPIView.as_view(), name='barber-list'),
	# path('barber/create/', views.BarberAPIView.as_view(), name='barber-create'),
	# path(r'^ratings/', include('star_ratings.urls', namespace='ratings', barber_api='ratings')).
	path('', include(router.urls))
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)