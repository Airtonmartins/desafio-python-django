from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator
from django.db import models

from .constants import EMAIL_EXISTS
from .managers import UserManager



class TimeStampedUserModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, TimeStampedUserModel):
    email = models.EmailField(
        unique=True, error_messages={'unique': EMAIL_EXISTS}
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'

    objects =  UserManager()


class Phone(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='phones'
    )
    number = models.PositiveIntegerField(
        validators=[MaxValueValidator(999999999)]
    )
    area_code = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    country_code = models.CharField(max_length=4)