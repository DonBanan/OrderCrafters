from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    experience = models.CharField(max_length=200)
    is_customer = models.BooleanField(default=False)
    is_performer = models.BooleanField(default=False)
