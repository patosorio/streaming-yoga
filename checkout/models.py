import uuid
from django.db import models
from membership.models import Membership
from django.contrib.auth.models import User
from datetime import datetime

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(
        max_length=255, null=False, blank=False, default="")
    stripeid = models.CharField(max_length=255, null=False, blank=False)
    stripe_subscription_id = models.CharField(
        max_length=255, null=False, blank=False)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
