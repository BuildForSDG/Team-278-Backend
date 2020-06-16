import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
# Create your models here.

# Database for all the farmers #
class Farmer(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    full_description = models.TextField(null=True)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=6)
    fax= models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=50)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.lastname
