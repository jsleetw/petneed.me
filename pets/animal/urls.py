# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^home', 'animal.views.home'),
    url(r'^get_img', 'animal.views.get_img'),
)
