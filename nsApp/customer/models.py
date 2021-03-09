from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    phone = models.IntegerField(blank=True)