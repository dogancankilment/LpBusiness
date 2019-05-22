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

                       url(r'^new-customer',
                           'home.views.new_customer',
                           name='new_customer'),

                       url(r'^new-partner',
                           'home.views.new_partner',
                           name='new_partner'),

                       url(r'^new-vendor',
                           'home.views.new_vendor',
                           name='new_vendor'),

                       url(r'^new-presale',
                           'home.views.new_presale',
                           name='new_presale'),

                       url(r'^new-postsale',
                           'home.views.new_postsale',
                           name='new_postsale'),

                       url(r'^new-case',
                           'home.views.new_case',
                           name='new_case'),

                       url(r'^new-support',
                           'home.views.new_support',
                           name='new_support'),

                       url(r'^show-customer',
                           'home.views.show_customers',
                           name='show_customers'),

                       url(r'^show-partner',
                           'home.views.show_partners',
                           name='show_partners'),

                       url(r'^show-vendor',
                           'home.views.show_vendors',
                           name='show_vendors'),

                       url(r'^show-presale',
                           'home.views.show_presales',
                           name='show_presales'),

                       url(r'^show-postsales',
                           'home.views.show_postsales',
                           name='show_postsales'),

                       url(r'^show-case',
                           'home.views.show_case',
                           name='show_case'),

                       url(r'^show-support',
                           'home.views.show_support',
                           name='show_support'),

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