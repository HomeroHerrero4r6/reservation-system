from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.
from Client.models import Client
from BillingMethod.models import Billing
from Room.models import Room
# django-ckeditor

class Reservation(models.Model):
    """Work experience model."""

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.OneToOneField(Room,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    total=BooleanField()
    billing_data=models.OneToOneField(Billing,on_delete=models.CASCADE)
    def __str__(self):
        """Return client room  - start Date and End Date"""
        return f'{self.client} {self.room}'