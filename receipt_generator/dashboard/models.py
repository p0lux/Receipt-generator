from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255)
    sudo = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(default='', max_length=255)
    address = models.TextField(blank=False, null=False)
    surface = models.IntegerField(blank=False, null=False)
    informations = models.TextField(default='')
    price = models.FloatField(blank=False, null=False)
    charges = models.FloatField(blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tenant(models.Model):
    firstname = models.CharField(max_length=255, blank=False, null=False)
    lastname = models.CharField(max_length=255, blank=False, null=False)
    home_id = models.ForeignKey(Home, on_delete=models.PROTECT, default='')
    phone = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Receipt(models.Model):
    filename = models.TextField(default="", blank=False, null=False)
    tenant_id = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    home_id = models.ForeignKey(Home, on_delete=models.PROTECT)
    datetime = models.DateTimeField(auto_now=timezone.now())
    send = models.BooleanField(default=False)

    def __str__(self):
        return self.filename
