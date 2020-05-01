from django.db import models

# Create your models here.


class Bicycle(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    company_id = models.CharField(max_length=255, null=False, blank=False)
    company_name = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)