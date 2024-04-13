from django.db import models
from django.contrib.auth.models import User


class Vendor(User):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __repr__(self):
        return self.name + " " + self.address



