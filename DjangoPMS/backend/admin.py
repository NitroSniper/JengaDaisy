from django.contrib import admin
from .models import Admin, Driver
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

admin.site.register(
    Driver
)


admin.site.register(
    Admin, LeafletGeoAdmin
)
