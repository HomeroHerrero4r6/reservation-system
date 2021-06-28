from django.db import models
from django.db.models.fields import BooleanField, EmailField

# Create your models here.
from Client.models import Client
# django-ckeditor

class Billing(models.Model):
    """Work experience model."""

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    adress = models.CharField(max_length=250)
    country=models.CharField(max_length=25)
    county=models.CharField(max_length=25)
    email=EmailField()
    bank=models.CharField(max_length=40)
    def __str__(self):
        """Return client and email"""
        return f'{self.client} {self.email} '