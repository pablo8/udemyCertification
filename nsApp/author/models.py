from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=300, blank=True)
    last_name = models.CharField(max_length=300, blank=True)
    phone_number = models.IntegerField(default=True)

