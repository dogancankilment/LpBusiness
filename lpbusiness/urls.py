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