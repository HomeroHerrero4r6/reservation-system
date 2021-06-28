from django.db import models

# Create your models here.

# django-ckeditor

class Room(models.Model):
    """Work experience model."""

    num = models.IntegerField()
    capacity = models.IntegerField()
    abailavility=models.BooleanField()
    description=models.CharField(max_length=250)
    def __str__(self):
        """Return room num  - capacity and availability"""
        return f'{self.num} {self.capacity} | {self.abailavility}'