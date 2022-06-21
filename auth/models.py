from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

# Create your models here.
class FndUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        fndUser = self.model(username=username, email=self.normalize_email(email), first_name=first_name)
        fndUser.set_password(password)
        fndUser.save()

        return fndUser

    def create_superuser(self, username, email, password):
      if password is None:
          raise TypeError('Superusers must have a password.')

      user = self.create_user(username, email, password)
      user.is_superuser = True
      user.is_staff = True
      user.is_verified=True
      user.save()

      return user