from django.db import models

# Create your models here.
from bicycles.models import Bicycle


class Rent(models.Model):
    bicycle = models.ForeignKey(Bicycle, null=False, blank=False, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255, null=False, blank=False)
    rented_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    rented_ended_at = models.DateTimeField(null=True, blank=True)


class Payment(models.Model):
    rent = models.ForeignKey(Rent, null=False, blank=False, on_delete=models.CASCADE)
    amount = models.FloatField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    payed_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
