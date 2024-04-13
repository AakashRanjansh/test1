from django.contrib import admin
from .models import Service, Plan, Event, Vendorlist

# Register your models here.
admin.site.register([Service, Plan, Event, Vendorlist])