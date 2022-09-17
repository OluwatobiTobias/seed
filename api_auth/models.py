from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.apps import apps
from django.contrib.auth.hashers import make_password

class CustomUserManager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        return super(CustomUserManager, self).create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        return super(CustomUserManager, self).create_superuser(username, email, password, **extra_fields)

    def _create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model( email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = None
    password = models.CharField(max_length=200, null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [password]

    objects = CustomUserManager()
