import uuid
from django.db import models
from membership.models import Membership
from django.contrib.auth.models import User
from datetime import datetime


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    order_total = models.IntegerField(null=False, default=0)
    grand_total = models.IntegerField(null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using uuid
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        update grand total each time line item is added
        """
        self.order_total = self.lineitems.aggregate(
            "lineitem_total")['lineitem_total']
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if isn't hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
   
    def __str__(self):
        return self.order_number


class LineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, on_delete=models.CASCADE, related_name="lineitems")
    membership = models.ForeignKey(
        Membership, null=False, on_delete=models.CASCADE, related_name="lineitems")
    lineitem_total = models.IntegerField(null=False, default=0)
  
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total
        """
        self.lineitem_total = self.membership.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'MEMBERSHIP: {self.membership.name} on order {self.order.order_number}'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(
        max_length=255, null=False, blank=False, default="")
    stripeid = models.CharField(max_length=255, null=False, blank=False)
    stripe_subscription_id = models.CharField(
        max_length=255, null=False, blank=False)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
