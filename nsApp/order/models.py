from django.db import models
from nsApp.customer.models import Customer


class Order(models.Model):
    product = models.CharField(max_length=300, blank=True)
    quantity = models.IntegerField(blank=True, default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
