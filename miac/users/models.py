from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self,
                    username,
                    email,
                    first_name,
                    last_name,
                    role,
                    password=None):

        if username is None:
            raise TypeError("Users must have a username.")

        if email is None:
            raise TypeError("Users must have an email address.")

        if first_name is None:
            raise TypeError("Users must have a first name.")

        if last_name is None:
            raise TypeError("Users must have a second name.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, first_name, last_name,
                         password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, email, first_name, last_name, 'Admin',
                                password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
    )

    username = PhoneNumberField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=50, choices=ROLES, null=True, default='Patient')

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return str(self.username)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
