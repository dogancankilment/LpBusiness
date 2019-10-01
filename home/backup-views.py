# all_customers = Customer.objects.all()
# all_vendors = Vendor.objects.all()
# all_partners = Partner.objects.all()
# len_customers = len(all_customers)
# len_vendors = len(all_vendors)
# len_partners = len(all_partners)
#
# t = {"request": request,
# "len_customers": len_customers,
# "len_partners": len_partners,
# "len_vendors": len_vendors}


# elif request.POST["new_account_manager"] != "":
#     new_vendor = Vendor()
#     new_vendor.company = request.POST["new_account_manager"]
#     new_vendor.fullname = ""
#     new_vendor.mail = ""
#     new_vendor.phone = ""
#     new_vendor.save()
#
#     new_activity.account_manager = new_vendor

# elif request.POST["new_partner"] != "":
#     new_partner = Partner()
#     new_partner.company = request.POST["new_partner"]
#     new_partner.fullname = ""
#     new_partner.mail = ""
#     new_partner.phone = ""
#     new_partner.save()
#
#     new_activity.partner = new_partner


# elif request.POST["new_customer"] != "":
#     new_customer = Customer()
#     new_customer.company = request.POST["new_customer"]
#     new_customer.fullname = ""
#     new_customer.mail = ""
#     new_customer.phone = ""
#     new_customer.save()
#
#     new_activity.customer = new_customer

# elif request.POST["new_customer"] != "":
#     new_customer = Customer()
#     new_customer.fullname = request.POST["new_customer"]
#     new_customer.mail = ""
#     new_customer.phone = ""
#     new_customer.save()
#
#     current_obj.customer = new_customer

# elif request.POST["new_partner"] != "":
#     new_partner = Partner()
#     new_partner.fullname = request.POST["new_partner"]
#     new_partner.mail = ""
#     new_partner.phone = ""
#     new_partner.save()
#
#     current_obj.partner = new_partner
#
# elif request.POST["new_vendor"] != "":
#     new_vendor = Vendor()
#     new_vendor.fullname = request.POST["new_vendor"]
#     new_vendor.mail = ""
#     new_vendor.phone = ""
#     new_vendor.save()
#
#     current_obj.vendor = new_vendor
