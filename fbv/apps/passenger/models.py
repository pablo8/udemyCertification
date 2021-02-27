from django.db import models


class Passenger(models.Model):
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    travel_points = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=3)

    def __str__(self):
        return self.first_name + self.last_name
