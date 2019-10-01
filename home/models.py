"""
    LpBusiness Database Design


    Vendor_Account_Manager
    -
    id pk int
    title string
    mail string
    phone string
    partner int FK >- Partner_Contact.id
    customer FK >- Customer_Contact.id int

    Partner_Contact
    -
    id pk int
    title string
    mail string
    phone string
    customer int FK >- Customer_Contact.id
    vendor int FK >- Vendor_Account_Manager.id

    Customer_Contact
    -
    id pk int
    title string
    mail string
    phone string

    Project
    -
    id pk int
    title string
    product string
    date string
    notes string
    extra string
    status boolean

"""
from django.db import models


class Customer(models.Model):
    brand = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.CharField(max_length=100)


class Partner(models.Model):
    brand = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.CharField(max_length=100)


class Vendor(models.Model):
    company = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.CharField(max_length=100)


class Officer(models.Model):
    fullname = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.CharField(max_length=100)


class ActivityType(models.Model):
    title = models.CharField(max_length=100)


class Activity(models.Model):
    vendor = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    account_manager = models.ForeignKey(Vendor, blank=True, null=True)
    partner = models.ForeignKey(Partner, blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    officer = models.ForeignKey(Officer, blank=True, null=True)
    activity = models.ForeignKey(ActivityType, blank=True, null=True)
    location = models.CharField(max_length=100)
