from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class user_membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=260)
    stripe_subscription_id = models.CharField(max_length=260)
    cancel_at_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)

