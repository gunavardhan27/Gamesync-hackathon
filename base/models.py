from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    field = (
        ('player','player'),
        ('sponsor','sponsor')
    )
    option = models.CharField(max_length=100,null=True,choices=field)

    def __str__(self):
        return self.username
