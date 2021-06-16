import django.contrib.auth.password_validation as validators
from django.core import exceptions
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.Serializer):
    username = PhoneNumberField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True, max_length=255)
    last_name = serializers.CharField(required=True, max_length=255)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(
                "The two password fields didn't match.")

        password = data.get("password1")

        errors = dict()
        try:
            validators.validate_password(password=password, user=User)
        except exceptions.ValidationError as e:
            errors["password"] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "password": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
        }

    def save(self, request):
        cleaned_data = self.get_cleaned_data()
        user = User.objects.create_user(**cleaned_data)
        return user
