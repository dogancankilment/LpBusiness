from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


def activity(request):
    if request.POST:
        new_activity = Activity()

        new_activity.date = request.POST["datepicker-autoclose"]

        if request.POST.has_key("tech"):
            tech = Tech.objects.get(id=request.POST["tech"])
            new_activity.tech = tech

        new_activity.activity = request.POST["activity"]
        new_activity.work = request.POST["work"]
        new_activity.brand = request.POST["brand"]

        if request.POST.has_key("existing_account_managers"):
            account_manager = AccountManager.objects.get(id=request.POST["existing_account_managers"])
            new_activity.account_manager = account_manager

        if request.POST.has_key("existing_partners"):
            partner = Partner.objects.get(id=request.POST["existing_partners"])
            new_activity.partner = partner

        if request.POST.has_key("existing_customers"):
            customer = Customer.objects.get(id=request.POST["existing_customers"])
            new_activity.customer = customer

        new_activity.activity = request.POST["product"]
        new_activity.work = request.POST["notes"]
        new_activity.brand = request.POST["actions"]

        new_activity.save()

        # return redirect(reverse(follow_list))
        return HttpResponse("success")

    account_managers = AccountManager.objects.all()
    partners = Partner.objects.all()
    customers = Customer.objects.all()
    techs = Tech.objects.all()

    c = {"request": request,
         "account_managers": account_managers,
         "partners": partners,
         "customers": customers,
         "techs": techs
         }

    c.update(csrf(request))

    return render_to_response("new/new-activity.html", c)