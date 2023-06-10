from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    def get_data(self):
        return {
            'username': self.username,
            'first_name': self.first_name,
        }
