from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Barber, Service, Appointment
from datetime import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


def get_token(user):
        refresh = RefreshToken.for_user(user)
        return refresh.access_token

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'access',]
    
    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        validated_data["access"] = get_token(new_user)
        Barber.objects.create(user=new_user)
        return validated_data

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    barber_name = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    services = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    customer_address = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields = ['id', 'barber_name', 'customer_name', 'customer_address', 'date_and_time', 'available', 'services']

    def get_barber_name(self, obj):
        return obj.barber.user.first_name

    def get_customer_name(self, obj):
        if obj.user:
            return obj.user.user.first_name
        else:
            return ("")

    def get_customer_address(self, obj):
        return obj.user.address

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date_and_time']


class AppointmentTimeSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields = ['time', 'id', 'available']

    def get_time(self, obj):
        return str(obj.date_and_time.time())

class BarberSerializer(serializers.ModelSerializer):

	name = serializers.SerializerMethodField()
	appointments = serializers.SerializerMethodField()
	services = serializers.SerializerMethodField()
	class Meta:
		model = Barber
		fields = ['user', 'name', 'image','nationality', 'telephone', 'credit', 'experience', 'services', 'appointments']

	def get_name(self, obj):
		return "%s %s"%(obj.user.first_name, obj.user.last_name)

	def get_appointments(self, obj):
		appointments = obj.barber_appointments.all().order_by('date_and_time')
		if appointments:
			date = appointments[0].date_and_time.date()
			dictionary = { 'dates' : 
				[] 
			}
			changed = True
			app_list = []
			for a in appointments:
				# print (a.date_and_time.date())
				if a.date_and_time.date() == date:
					print("appending")
					print(a.date_and_time.date())
					app_list.append(AppointmentTimeSerializer(a).data)
				else:
					print("clearing")
					print(a.date_and_time.date())
					dictionary["dates"].append({"date":str(date), "times":app_list})
					date = a.date_and_time.date()
					app_list = []
					app_list.append(AppointmentTimeSerializer(a).data)
					dictionary[str(date)] = app_list

			return dictionary

	def get_services(self, obj):
		services = obj.services.all()
		return ServiceSerializer(services, many=True).data



class BarberProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    future_appointments = serializers.SerializerMethodField()
    past_appointments = serializers.SerializerMethodField()

    class Meta:
        model = Barber
        fields = ['user', 'name', 'image','nationality', 'telephone', 'credit', 'experience', 'services', 'future_appointments', 'past_appointments']

    def get_name(self, obj):
        return "%s %s"%(obj.user.first_name, obj.user.last_name)

    def get_future_appointments(self, obj):
        past_appointments = obj.barber_appointments.filter(date_and_time__gte=datetime.now())
        return AppointmentSerializer(past_appointments, many=True).data	

    def get_past_appointments(self, obj):
        past_appointments = obj.barber_appointments.filter(date_and_time__lte=datetime.now())
        return AppointmentSerializer(past_appointments, many=True).data

    def get_services(self, obj):
        services = obj.services.all()
        return ServiceSerializer(services, many=True).data

    

class BarberAppointmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['total_price']

class BarberAppointmentsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    appointments = serializers.SerializerMethodField()
    class Meta:
        model = Barber
        fields = ['user', 'name', 'image','nationality', 'telephone', 'experience', 'services', 'appointments']

    def get_name(self, obj):
        return "%s %s"%(obj.user.first_name, obj.user.last_name)

    def get_appointments(self, obj):
        date = datetime.now()
        obj.barber_appointments.all()
        returm
        

