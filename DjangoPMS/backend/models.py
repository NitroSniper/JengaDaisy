from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.

class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Admin(BaseUser):
    location = gis_models.PointField(srid=4326, default=None)


class Driver(BaseUser):
    credits = models.PositiveIntegerField(default=100)

class ParkingLot(models.Model):
    poly = gis_models.PolygonField()
    name = models.CharField()
