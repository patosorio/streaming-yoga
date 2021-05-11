from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Membership(models.Model):
    id = models.CharField(max_length=254, blank=True, primary_key=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    subscription_type = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.subscription_type


