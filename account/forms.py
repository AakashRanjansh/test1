from django import forms
from django.db import models
from datetime import datetime
from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model=Vendor 
        fields=["username", "password", "address", "phone", "email"]
