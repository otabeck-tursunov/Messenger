from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    t_sana = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
