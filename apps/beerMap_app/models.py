from __future__ import unicode_literals
from django.db import models

class Brewery(models.Model):
    name = models.CharField(max_length=255)
    coords = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)

    allows_kids = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return f"<Brewery object: {self.name} - {self.coords} - {self.address}>"

class Style(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Container(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Beer(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    abv = models.DecimalField(decimal_places=1, max_digits=5)
    ibu = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    brewery = models.OneToOneField(Brewery)
    containers = models.ManyToManyField(Container, related_name="beers")
    style = models.ForeignKey(Style, related_name="beers")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

