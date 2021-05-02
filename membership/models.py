from django.conf import settings
from django.db import models


MEMBERSHIPS_OPTIONS = [
    ("Free", "Free"),
    ("Professional", "Pro")
]


class Membership(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    type_member = models.CharField(
        choices=MEMBERSHIPS_OPTIONS,
        default="Free",
        max_length=50)
    price = models.IntegerField(default=29.99)
    stripe_plan_id = models.CharField(max_length=50)

    def __str__(self):
        return self.type_member


class UserMembership(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_client_id = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username

