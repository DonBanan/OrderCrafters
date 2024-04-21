from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    experience = models.CharField(max_length=200)
    is_customer = models.BooleanField(default=False)
    is_performer = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def formatted_name(self):
        return f"{self.last_name} {self.first_name[0]}." if self.last_name else self.username
