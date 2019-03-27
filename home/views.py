from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def home(request):
    all_customers = Customer.objects.all()
    all_vendors = Vendor.objects.all()
    all_partners = Partner.objects.all()

    len_customers = len(all_customers)
    len_vendors = len(all_vendors)
    len_partners = len(all_partners)

    c = {"request": request,
         "len_customers": len_customers,
         "len_partners": len_partners,
         "len_vendors": len_vendors}

    c.update(csrf(request))

    return render_to_response("home/home.html", c)


def new_customer(request):
    page_title = "Customer"

    if request.POST:
        new_one = Customer()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title}

    c.update(csrf(request))

    return render_to_response("home/add-new.html", c)


def new_partner(request):
    page_title = "Partner"

    if request.POST:
        new_one = Partner()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title}

    c.update(csrf(request))

    return render_to_response("home/add-new.html", c)


def new_vendor(request):
    page_title = "Vendor"

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title}

    c.update(csrf(request))

    return render_to_response("home/add-new.html", c)


def new_presale(request):
    page_title = "PreSale"

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title}

    c.update(csrf(request))

    return render_to_response("home/add-new.html", c)


def new_postsale(request):
    page_title = "PostSale"

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title}

    c.update(csrf(request))

    return render_to_response("home/add-new.html", c)


def new_case(request):
    page_title = "Case"

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title}

    c.update(csrf(request))

    return render_to_response("home/add-new.html", c)


def new_support(request):
    page_title = "Support"

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title}

    c.update(csrf(request))

    return render_to_response("home/add-new.html", c)


def show_customers(request):
    return render_to_response("home/blank.html")


def show_partners(request):
    return render_to_response("home/blank.html")


def show_vendors(request):
    return render_to_response("home/blank.html")


def show_presales(request):
    return render_to_response("home/blank.html")


def show_postsales(request):
    return render_to_response("home/blank.html")


def show_case(request):
    return render_to_response("home/blank.html")


def show_support(request):
    return render_to_response("home/blank.html")