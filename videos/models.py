from django.db import models
from membership.models import Membership


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Video(models.Model):
    category = models.ManyToManyField(Category)
    membership = models.ManyToManyField(Membership)
    title = models.CharField(max_length=300)
    description = models.TextField()
    duration = models.DurationField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
        