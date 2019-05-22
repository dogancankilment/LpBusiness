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
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    c = {"request": request,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("home/home.html", c)


def new_customer(request):
    page_title = "Customer"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    if request.POST:
        new_one = Customer()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("new/new-customer.html", c)


def new_partner(request):
    page_title = "Partner"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    if request.POST:
        new_one = Partner()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("new/new-partner.html", c)


def new_vendor(request):
    page_title = "Vendor"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("new/new-vendor.html", c)


def new_presale(request):
    page_title = "Presales"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("new/new-presale.html", c)


def new_postsale(request):
    page_title = "PostSale"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("new/new-postsale.html", c)


def new_case(request):
    page_title = "Case"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("new/new-case.html", c)


def new_support(request):
    page_title = "Support"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    if request.POST:
        new_one = Vendor()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(home))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("new/new-support.html", c)


def show_customers(request):
    page_title = "Customers"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    all = Customer.objects.all()

    c = {"request": request,
         "page_title": page_title,
         "all": all,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("show/show-customers.html", c)


def show_partners(request):
    page_title = "Partners"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("show/show-customers.html", c)


def show_vendors(request):
    page_title = "Vendors"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("show/show-customers.html", c)


def show_presales(request):
    page_title = "Pre-Sales"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("show/show-customers.html", c)


def show_postsales(request):
    page_title = "Post-Sales"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("show/show-customers.html", c)


def show_case(request):
    page_title = "Case"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("show/show-customers.html", c)


def show_support(request):
    page_title = "Support"

    # counts
    customers_count = len(Customer.objects.all())
    vendor_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    presales_count = len(PreSales.objects.all())
    postsales_count = len(PostSales.objects.all())
    case_count = len(Case.objects.all())
    support_count = len(Support.objects.all())

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendor_count": vendor_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count}

    c.update(csrf(request))

    return render_to_response("show/show-customers.html", c)
