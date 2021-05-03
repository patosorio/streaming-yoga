import uuid
from django.db import models
from django.conf import settings
from django.db.models import Sum
from membership.models import Membership


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    order_total = models.IntegerField(null=False)
    
    def _generate_order_number(self):
        """
        Generate a random, unique order number using uuid
        """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """update grand total each time"""
        self.order_total = self.lineitems.aggregate('lineitem_total')
        self.save()

    def save(self, *args, **kwargs):
        """ override the original save methd to set the order number it doesn't exist """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    membership = models.ForeignKey(Membership, null=False, blank=False, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        """override the original save methd to set the order number ix doesn't exist"""

        self.lineitem_total = self.membership.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f' {self.membership.name} on order {self.order.order_number}'
