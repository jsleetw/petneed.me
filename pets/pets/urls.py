from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
import animal.urls
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # urls specific to this app
    url(r'^animal/', include("animal.urls", namespace="animal")),
    # catch all, redirect to myfirstapp home view
    #url(r'.*', redirect_to, {'url': '/animal/home'}),

    # Examples:
    url(r'^$', 'animal.views.home', name='home'),
    # catch all, redirect to myfirstapp home view
    #url(r'.*', redirect_to, {'url': '/'}),

    # url(r'^pets/', include('pets.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
