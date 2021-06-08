
from django.db import models
from django.contrib.auth.models import AbstractUser
from djstripe.models import Customer, Subscription


# Create your models here.


class User(AbstractUser):
    customer = models.ForeignKey(
        'djstripe.Customer', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Customer object, if it exists",
        related_name='topic_content_type'
    )
    subscription = models.ForeignKey(
        'djstripe.Subscription', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Subscription object, if it exists",
        related_name='topic_content_type'
    )
