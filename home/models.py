from django.db import models


class Tech(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)


class AccountManager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)


class Partner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=100)


class ActivityType(models.Model):
    title = models.CharField(max_length=100)


class Activity(models.Model):
    date = models.CharField(max_length=100)
    tech = models.ForeignKey(Tech, blank=True, null=True)
    activity = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    account_manager = models.ForeignKey(AccountManager, max_length=100)
    partner = models.ForeignKey(Partner, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    product = models.ForeignKey(Product, blank=True, null=True)
    notes = models.CharField(max_length=100)
    actions = models.CharField(max_length=100)