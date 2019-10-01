from django.shortcuts import render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


@login_required()
def home(request):
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    total_sales = presales_count + postsales_count

    c = {"request": request,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "total_sales": total_sales,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("home/home.html", c)


@login_required()
def new_activity_type(request):
    page_title = "Activity Type"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    if request.POST:
        new_one = ActivityType()
        new_one.title = request.POST["title"]

        new_one.save()

        return redirect(reverse(show_activity_types))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("new/new-activity-type.html", c)


@login_required()
def choose_brand_for_activity(request):
    return render_to_response("new/brand-choice-activity.html")


@login_required()
def choose_brand_for_customer(request):
    return render_to_response("show/brand-choice-customer.html")


@login_required()
def choose_brand_for_vendor(request):
    return render_to_response("show/brand-choice-vendor.html")


@login_required()
def choose_brand_for_partner(request):
    return render_to_response("show/brand-choice-partner.html")


@login_required()
def new_customer(request):
    page_title = "Customer"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    if request.POST:
        new_one = Customer()
        new_one.company = request.POST["company"]
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(show_customers))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("new/new-customer.html", c)


@login_required()
def new_partner(request):
    page_title = "Partner"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    if request.POST:
        new_one = Partner()
        new_one.company = request.POST["company"]
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(show_partners))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("new/new-partner.html", c)


@login_required()
def new_vendor(request):
    page_title = "Vendor"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))
    officers_count = len(Officer.objects.all())

    if request.POST:
        new_one = Vendor()
        new_one.company = request.POST["company"]
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(show_vendors))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("new/new-vendor.html", c)


@login_required()
def new_officer(request):
    page_title = "Officer"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))
    officers_count = len(Officer.objects.all())

    if request.POST:
        new_one = Officer()
        new_one.fullname = request.POST["fullname"]
        new_one.mail = request.POST["email"]
        new_one.phone = request.POST["phone"]
        new_one.save()

        return redirect(reverse(show_officers))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("new/new-officer.html", c)


@login_required()
def mobileiron_new_activity(request):
    page_title = "Activity"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    all_customers = Customer.objects.all()
    # all_vendors = Vendor.objects.all()
    # all_partners = Partner.objects.all()
    all_vendors = Vendor.objects.filter(company__contains="MobileIron")
    all_partners = Partner.objects.filter(company__contains="MobileIron")

    all_officers = Officer.objects.all()
    all_activity_types = ActivityType.objects.all()

    if request.POST:
        new_activity = Activity()

        # new_activity.vendor = request.POST["vendor"]
        new_activity.vendor = "MobileIron"
        new_activity.product = request.POST["product"]
        new_activity.description = request.POST["description"]
        new_activity.status = request.POST["status"]
        new_activity.date = request.POST["datepicker-autoclose"]

        if request.POST.has_key("existing_customers"):
            current_customer = Customer.objects.get(id=request.POST["existing_customers"])
            new_activity.customer = current_customer

        if request.POST.has_key("existing_partners"):
            current_partner = Partner.objects.get(id=request.POST["existing_partners"])
            new_activity.partner = current_partner

        if request.POST.has_key("existing_account_managers"):
            current_vendor = Vendor.objects.get(id=request.POST["existing_account_managers"])
            new_activity.account_manager = current_vendor

        if request.POST.has_key("officer"):
            current_officer = Officer.objects.get(id=request.POST["officer"])
            new_activity.officer = current_officer

        if request.POST.has_key("activitytype"):
            current_activity_type = ActivityType.objects.get(id=request.POST["activitytype"])
            new_activity.activity = current_activity_type

        new_activity.location = request.POST["location"]

        new_activity.save()

        return redirect(reverse(show_activities))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "all_customers": all_customers,
         "all_partners": all_partners,
         "all_vendors": all_vendors,
         "all_activity_types": all_activity_types,
         "officers_count": officers_count,
         "all_officers": all_officers,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("new/new-activity.html", c)


@login_required()
def trendmicro_new_activity(request):
    page_title = "Activity"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    all_customers = Customer.objects.all()
    # all_vendors = Vendor.objects.all()
    # all_partners = Partner.objects.all()
    all_vendors = Vendor.objects.filter(company__contains="Trend Micro")
    all_partners = Partner.objects.filter(company__contains="Trend Micro")
    all_officers = Officer.objects.all()
    all_activity_types = ActivityType.objects.all()

    if request.POST:
        new_activity = Activity()

        # new_activity.vendor = request.POST["vendor"]
        new_activity.vendor = "Trend Micro"
        new_activity.product = request.POST["product"]
        new_activity.description = request.POST["description"]
        new_activity.status = request.POST["status"]
        new_activity.date = request.POST["datepicker-autoclose"]

        if request.POST.has_key("existing_customers"):
            current_customer = Customer.objects.get(id=request.POST["existing_customers"])
            new_activity.customer = current_customer

        if request.POST.has_key("existing_partners"):
            current_partner = Partner.objects.get(id=request.POST["existing_partners"])
            new_activity.partner = current_partner

        if request.POST.has_key("existing_account_managers"):
            current_vendor = Vendor.objects.get(id=request.POST["existing_account_managers"])
            new_activity.account_manager = current_vendor

        if request.POST.has_key("officer"):
            current_officer = Officer.objects.get(id=request.POST["officer"])
            new_activity.officer = current_officer

        if request.POST.has_key("activitytype"):
            current_activity_type = ActivityType.objects.get(id=request.POST["activitytype"])
            new_activity.activity = current_activity_type

        new_activity.location = request.POST["location"]

        new_activity.save()

        return redirect(reverse(show_activities))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "all_customers": all_customers,
         "all_partners": all_partners,
         "all_vendors": all_vendors,
         "all_activity_types": all_activity_types,
         "officers_count": officers_count,
         "all_officers": all_officers,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("new/new-activity.html", c)



@login_required()
def show_activity_types(request):
    page_title = "Activity Types"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))
    officers_count = len(Officer.objects.all())

    all = ActivityType.objects.all()

    c = {"request": request,
         "page_title": page_title,
         "all": all,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("show/show-activity-types.html", c)


@login_required()
def show_customers(request, choice):
    page_title = "Customers"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))
    officers_count = len(Officer.objects.all())

    if choice == "all":
        all = Customer.objects.all()

    elif choice == "Trend Micro":
        all = Customer.objects.all()

    else:
        all = Customer.objects.all()
    c = {"request": request,
         "page_title": page_title,
         "all": all,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("show/show-customers.html", c)


@login_required()
def show_officers(request):
    page_title = "Officers"

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    all_officers = Officer.objects.all()

    c = {"request": request,
         "page_title": page_title,
         "all": all_officers,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("show/show-officers.html", c)


@login_required()
def show_partners(request):
    page_title = "Partners"

    all = Partner.objects.all()

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))
    officers_count = len(Officer.objects.all())

    c = {"request": request,
         "page_title": page_title,
         "all": all,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("show/show-partners.html", c)


@login_required()
def show_vendors(request):
    page_title = "Vendors"

    all_vendors = Vendor.objects.all()

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    c = {"request": request,
         "page_title": page_title,
         "all": all_vendors,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("show/show-vendors.html", c)


@login_required()
def show_activities(request):
    page_title = "Activities"

    all_activities = Activity.objects.all()

    # counts
    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    c = {"request": request,
         "page_title": page_title,
         "customers_count": customers_count,
         "vendors_count": vendors_count,
         "partners_count": partners_count,
         "presales_count": presales_count,
         "postsales_count": postsales_count,
         "case_count": case_count,
         "support_count": support_count,
         "officers_count": officers_count,
         "all": all_activities,
         "activities_count": activities_count}

    c.update(csrf(request))

    return render_to_response("show/show-activities.html", c)


@login_required()
def edit_customer(request, id):
    current_obj = Customer.objects.get(id=id)

    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    if request.POST:
        # current_obj.fullname = form.cleaned_data.get('title')
        current_obj.company = request.POST["company"]
        current_obj.fullname = request.POST["fullname"]
        current_obj.mail = request.POST["email"]
        current_obj.phone = request.POST["phone"]
        current_obj.save()

        return redirect(reverse(show_customers))

    else:
        c = {"request": request,
             "customers_count": customers_count,
             "vendors_count": vendors_count,
             "partners_count": partners_count,
             "presales_count": presales_count,
             "postsales_count": postsales_count,
             "case_count": case_count,
             "support_count": support_count,
             "fullname": current_obj.fullname,
             "mail": current_obj.mail,
             "company": current_obj.company,
             "phone": current_obj.phone,
             "officers_count": officers_count,
             "activities_count": activities_count}

        c.update(csrf(request))

    return render_to_response('edit/edit-customer.html', c)


@login_required()
def edit_partner(request, id):
    current_obj = Partner.objects.get(id=id)

    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    if request.POST:
        # current_obj.fullname = form.cleaned_data.get('title')
        current_obj.company = request.POST["company"]
        current_obj.fullname = request.POST["fullname"]
        current_obj.mail = request.POST["email"]
        current_obj.phone = request.POST["phone"]
        current_obj.save()

        return redirect(reverse(show_partners))

    else:
        c = {"request": request,
             "customers_count": customers_count,
             "vendors_count": vendors_count,
             "partners_count": partners_count,
             "presales_count": presales_count,
             "postsales_count": postsales_count,
             "case_count": case_count,
             "support_count": support_count,
             "fullname": current_obj.fullname,
             "mail": current_obj.mail,
             "phone": current_obj.phone,
             "company": current_obj.company,
             "officers_count": officers_count,
             "activities_count": activities_count}

        c.update(csrf(request))

    return render_to_response('edit/edit-partner.html', c)


@login_required()
def edit_activity_type(request, id):
    current_obj = ActivityType.objects.get(id=id)

    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    if request.POST:
        # current_obj.fullname = form.cleaned_data.get('title')
        current_obj.title = request.POST["title"]

        current_obj.save()

        return redirect(reverse(show_activity_types))

    else:
        c = {"request": request,
             "customers_count": customers_count,
             "vendors_count": vendors_count,
             "partners_count": partners_count,
             "presales_count": presales_count,
             "postsales_count": postsales_count,
             "case_count": case_count,
             "support_count": support_count,
             "title": current_obj.title,
             "officers_count": officers_count,
             "activities_count": activities_count}

        c.update(csrf(request))

    return render_to_response('edit/edit-activity-type.html', c)


@login_required()
def edit_vendor(request, id):
    current_obj = Vendor.objects.get(id=id)

    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    if request.POST:
        # current_obj.fullname = form.cleaned_data.get('title')
        current_obj.company = request.POST["company"]
        current_obj.fullname = request.POST["fullname"]
        current_obj.mail = request.POST["email"]
        current_obj.phone = request.POST["phone"]
        current_obj.save()

        return redirect(reverse(show_vendors))

    else:
        c = {"request": request,
             "customers_count": customers_count,
             "vendors_count": vendors_count,
             "partners_count": partners_count,
             "presales_count": presales_count,
             "postsales_count": postsales_count,
             "case_count": case_count,
             "support_count": support_count,
             "fullname": current_obj.fullname,
             "mail": current_obj.mail,
             "phone": current_obj.phone,
             "company": current_obj.company,
             "officers_count": officers_count,
             "activities_count": activities_count}

        c.update(csrf(request))

    return render_to_response('edit/edit-vendor.html', c)


@login_required()
def edit_officer(request, id):
    current_obj = Officer.objects.get(id=id)

    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    if request.POST:
        # current_obj.fullname = form.cleaned_data.get('title')
        current_obj.fullname = request.POST["fullname"]
        current_obj.mail = request.POST["email"]
        current_obj.phone = request.POST["phone"]
        current_obj.save()

        return redirect(reverse(show_officers))

    else:
        c = {"request": request,
             "customers_count": customers_count,
             "vendors_count": vendors_count,
             "partners_count": partners_count,
             "presales_count": presales_count,
             "postsales_count": postsales_count,
             "case_count": case_count,
             "support_count": support_count,
             "fullname": current_obj.fullname,
             "mail": current_obj.mail,
             "phone": current_obj.phone,
             "officers_count": officers_count,
             "activities_count": activities_count}

        c.update(csrf(request))

    return render_to_response('edit/edit-officer.html', c)


@login_required()
def edit_activity(request, id):
    current_obj = Activity.objects.get(id=id)

    customers_count = len(Customer.objects.all())
    vendors_count = len(Vendor.objects.all())
    partners_count = len(Partner.objects.all())
    officers_count = len(Officer.objects.all())
    activities_count = len(Activity.objects.all())

    # finding for presale id current string value
    presale = ActivityType.objects.get(title__contains="PreSale")
    presales_count = len(Activity.objects.filter(activity=presale.id))

    # finding for postsale id current string value
    postsale = ActivityType.objects.get(title__contains="PostSale")
    postsales_count = len(Activity.objects.filter(activity=postsale.id))

    # finding for case id current string value
    case = ActivityType.objects.get(title__contains="Case")
    case_count = len(Activity.objects.filter(activity=case.id))

    # finding for support id current string value
    support = ActivityType.objects.get(title__contains="Support")
    support_count = len(Activity.objects.filter(activity=support.id))

    total_sales = int(partners_count) + int(vendors_count)

    all_officers = Officer.objects.all()
    all_customers = Customer.objects.all()
    all_partners = Partner.objects.all()
    all_vendors = Vendor.objects.all()
    all_activity_types = ActivityType.objects.all()

    if request.POST:
        current_obj.company = request.POST["company"]
        current_obj.product = request.POST["product"]
        current_obj.description = request.POST["description"]
        current_obj.status = request.POST["status"]
        current_obj.date = request.POST["datepicker-autoclose"]

        if request.POST.has_key("existing_customers"):
            current_customer = Customer.objects.get(id=request.POST["existing_customers"])
            current_obj.customer = current_customer

        else:
            current_obj.customer = current_obj.customer

        if request.POST.has_key("existing_partners"):
            current_partner = Partner.objects.get(id=request.POST["existing_partners"])
            current_obj.partner = current_partner

        else:
            current_obj.partner = current_obj.partner

        if request.POST.has_key("existing_vendors"):
            current_vendor = Vendor.objects.get(id=request.POST["existing_vendors"])
            current_obj.vendor = current_vendor

        else:
            current_obj.vendor = current_obj.vendor

        if request.POST.has_key("officer"):
            current_officer = Officer.objects.get(id=request.POST["officer"])
            current_obj.officer = current_officer

        else:
            current_obj.officer = current_obj.officer

        if request.POST.has_key("activitytype"):
            current_activity_type = ActivityType.objects.get(id=request.POST["activitytype"])
            current_obj.activity = current_activity_type

        else:
            current_obj.activity = current_obj.activity

        current_obj.save()

        return redirect(reverse(show_activities))

    else:
        c = {"request": request,
             "customers_count": customers_count,
             "vendors_count": vendors_count,
             "partners_count": partners_count,
             "presales_count": presales_count,
             "postsales_count": postsales_count,
             "case_count": case_count,
             "support_count": support_count,
             "current_obj": current_obj,
             "officers_count": officers_count,
             "all_officers": all_officers,
             "all_customers": all_customers,
             "all_partners": all_partners,
             "all_vendors": all_vendors,
             "all_activity_types": all_activity_types,
             "total_sales": total_sales,
             "activities_count": activities_count}

        c.update(csrf(request))

    return render_to_response('edit/edit-activity.html', c)


@login_required()
def delete_customer(request, id):
    current_obj = Customer.objects.get(id=id)
    current_obj.delete()

    return redirect(reverse(show_customers))


@login_required()
def delete_vendor(request, id):
    current_obj = Vendor.objects.get(id=id)
    current_obj.delete()

    return redirect(reverse(show_vendors))


@login_required()
def delete_partner(request, id):
    current_obj = Partner.objects.get(id=id)
    current_obj.delete()

    return redirect(reverse(show_partners))


@login_required()
def delete_officer(request, id):
    current_obj = Officer.objects.get(id=id)
    current_obj.delete()

    return redirect(reverse(show_officers))


@login_required()
def delete_activity_type(request, id):
    current_obj = ActivityType.objects.get(id=id)
    current_obj.delete()

    return redirect(reverse(show_activity_types))


@login_required()
def delete_activity(request, id):
    current_obj = Activity.objects.get(id=id)
    current_obj.delete()

    return redirect(reverse(show_activities))