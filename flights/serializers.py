from rest_framework import serializers
from django.contrib.auth import get_user_model

from flights.models import Booking, Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["destination", "time", "price", "id"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "id"]


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "passengers", "id"]


class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["date", "passengers"]



User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    allow user to cretae new object
    """

    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ["username","password","first_name","last_name"]

        def create (self, validated_data):
            password = validated_data.pop("password")
            new_user = User(**validated_data)
            new_user.set_password(password)
            new_user.save()

            return validated_data