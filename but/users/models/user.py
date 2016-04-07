from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone_number = model.CharField(
            max_length=20,
    )

    description = models.TextField()

    def __str__(self):
        return self.username

    class Meta:

        verbose_name = "유저"
        verbose_name_plural = verbose_name
