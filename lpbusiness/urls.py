"""
    Customer:
        - Show
        - New
        - Edit
        - Delete

    Partner:
        - Show
        - New
        - Edit
        - Delete

    Vendor:
        - Show
        - New
        - Edit
        - Delete

    Officer:
        - Show
        - New
        - Edit
        - Delete

    Activity:
        - Show
        - New
        - Edit
        - Delete

    Activity Type:
        - Show
        - New
        - Edit
        - Delete

"""

from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^$',
                           'home.views.home',
                           name='home'),

                       url(r'^login',
                           'authentico.views.login',
                           name='login'),

                       url(r'^register',
                           'authentico.views.register',
                           name='register'),

                       url(r'^logout$',
                           'authentico.views.logout',
                           name='logout'),

                       url(r'^forgotpass',
                           'authentico.views.forgotpass',
                           name='forgotpass'),

                       # Block Customer

                       url(r'^show-customer-(?P<id>\w+)',
                           'home.views.show_customers',
                           name='show_customers'),

                       url(r'^customer-brand-choice',
                           'home.views.choose_brand_for_customer',
                           name='choose_brand_for_customer'),

                       url(r'^new-customer',
                           'home.views.new_customer',
                           name='new_customer'),

                       url(r'^edit-customer-(?P<id>\w+)',
                           'home.views.edit_customer',
                           name='edit_customer'),

                       url(r'^delete-customer-(?P<id>\w+)',
                           'home.views.delete_customer',
                           name='delete_customer'),

                       # Endblock Customer

                       # Block Partner

                       url(r'^new-partner',
                           'home.views.new_partner',
                           name='new_partner'),

                       url(r'^show-partner-(?P<id>\w+)',
                           'home.views.show_partners',
                           name='show_partners'),

                       url(r'^partner-brand-choice',
                           'home.views.choose_brand_for_partner',
                           name='choose_brand_for_partner'),

                       url(r'^edit-partner-(?P<id>\w+)',
                           'home.views.edit_partner',
                           name='edit_partner'),

                       url(r'^delete-partner-(?P<id>\w+)',
                           'home.views.delete_partner',
                           name='delete_partner'),

                       # EndBlock Partner

                       # Block Vendor

                       url(r'^new-vendor',
                           'home.views.new_vendor',
                           name='new_vendor'),

                       url(r'^show-vendor-(?P<id>\w+)',
                           'home.views.show_vendors',
                           name='show_vendors'),

                       url(r'^vendor-brand-choice',
                           'home.views.choose_brand_for_vendor',
                           name='choose_brand_for_vendor'),

                       url(r'^edit-vendor-(?P<id>\w+)',
                           'home.views.edit_vendor',
                           name='edit_vendor'),

                       url(r'^delete-vendor-(?P<id>\w+)',
                           'home.views.delete_vendor',
                           name='delete_vendor'),

                       # EndBlock Vendor

                       # Block Officer

                       url(r'^new-officer',
                           'home.views.new_officer',
                           name='new_officer'),

                       url(r'^show-officer',
                           'home.views.show_officers',
                           name='show_officers'),

                       url(r'^edit-officer-(?P<id>\w+)',
                           'home.views.edit_officer',
                           name='edit_officer'),

                       url(r'^delete-officer-(?P<id>\w+)',
                           'home.views.delete_officer',
                           name='delete_officer'),

                       # Block Activity

                       url(r'^trendmicro-new-activity',
                           'home.views.trendmicro_new_activity',
                           name='trendmicro_new_activity'),

                       url(r'^mobileiron-new-activity',
                           'home.views.mobileiron_new_activity',
                           name='mobileiron_new_activity'),

                       url(r'^new-activity',
                           'home.views.choose_brand',
                           name='choose_brand'),

                       url(r'^show-activity',
                           'home.views.show_activities',
                           name='show_activities'),

                       url(r'^edit-activity-(?P<id>\w+)',
                           'home.views.edit_activity',
                           name='edit_activity'),

                       url(r'^delete-activity-(?P<id>\w+)',
                           'home.views.delete_activity',
                           name='delete_activity'),

                       # EndBlock Activity

                       # Block Activity Type

                       url(r'^show-types',
                           'home.views.show_activity_types',
                           name='show_activity_types'),

                       url(r'^new-type',
                           'home.views.new_activity_type',
                           name='new_activity_type'),

                       url(r'^edit-type-(?P<id>\w+)',
                           'home.views.edit_activity_type',
                           name='edit_activity_type'),

                       url(r'^delete-type-(?P<id>\w+)',
                           'home.views.delete_activity_type',
                           name='delete_activity_type'),

                       # Endblock Activity Type

                       )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

if settings.DEBUG:   # if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )