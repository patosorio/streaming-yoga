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


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    membership = models.ForeignKey(Membership, null=False, blank=False, on_delete=models.CASCADE)

