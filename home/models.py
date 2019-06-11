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
    fullname = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.CharField(max_length=100)


class Partner(models.Model):
    fullname = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.CharField(max_length=100)


class Vendor(models.Model):
    fullname = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.CharField(max_length=100)


class PreSales(models.Model):
    company = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor)
    partner = models.ForeignKey(Partner)
    customer = models.ForeignKey(Customer)
    poc_product = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


class PostSales(models.Model):
    company = models.CharField(max_length=100)
    coming_from = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    postsale = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Support(models.Model):
    company = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    partner = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


class Case(models.Model):
    case_no = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    solution = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class DemoCenter(models.Model):
    # server, hostname, ip adress, domain, username, password, console username, password,
    server = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    console_username = models.CharField(max_length=100)
    console_password = models.CharField(max_length=100)


# class Project(models.Model):
#     title = models.CharField(max_length=100)
#     product = models.CharField(max_length=100)
#     information = models.CharField(max_length=100)
#     notes = models.TextField()
#     status = models.BooleanField(default=False)
#     customer = models.ForeignKey(Customer)
#     partner = models.ForeignKey(Partner)
#     vendor = models.ForeignKey(Vendor)
