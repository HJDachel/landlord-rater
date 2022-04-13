from django.db import models

# Create your models here.

class Property(models.Model):
    property_street_address = models.CharField(max_length=200)
    property_city_address = models.CharField(max_length=200)
    property_state_address = models.CharField(max_length=200)