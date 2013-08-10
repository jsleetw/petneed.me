# app specific urls
from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^home', 'animal.views.home'),
    url(r'^page/', 'animal.views.page'),
    url(r'^login', 'animal.views.login'),
    url(r'^API/0.1/animals/$', 'animal.views.get_animals'),
    url(r'^API/0.1/animal/(?P<accept_num>\d+)/$', 'animal.views.get_specific_animal'),
    url(r'^facebook_login', 'animal.views.facebook_login'),
    url(r'^register', 'animal.views.register'),
    #url(r'^get_img', 'animal.views.get_img'),
)
