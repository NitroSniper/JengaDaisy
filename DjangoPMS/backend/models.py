from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Admin(BaseUser):
    pass


class Driver(BaseUser):
    credits = models.PositiveIntegerField(default=100)