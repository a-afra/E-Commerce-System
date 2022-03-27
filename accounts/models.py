from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
# we create a custom user model
class AccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Customer must have a username.')

        user = self.model(username=username, email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    # todo provide a function for creating superuser


# our Customer model
class Customer(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=10)

    # unique identifier for Customer model
    # alternatively we can use email instead of username
    USERNAME_FIELD = 'username'
    objects = AccountManager()

    def __str__(self):
        return self.username
