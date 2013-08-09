from django.shortcuts import render_to_response
from models import Animal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
import urllib
import urllib2
from urllib2 import HTTPError
from django.http import HttpResponse
from django.conf import settings

def home(request):
    animals = Animal.objects.order_by("-id")
    paginator = Paginator(animals, 10)
    animals = paginator.page(1)
    print animals

    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]

    return render_to_response('index.html', {"animals": animals},
            context_instance=RequestContext(request) )

def page(request):
    page = int(request.path_info.strip('/animal/page/'))
    animals = Animal.objects.order_by("-id")
    paginator = Paginator(animals, 10)
    animals = paginator.page(page)
    print animals
    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]
    return render_to_response('page.html', {"animals": animals} )

def login(request):
      return render_to_response('login.html',
              context_instance=RequestContext(request))

def facebook_login(request):
    try:
        url = "https://graph.facebook.com/oauth/access_token"
        data = {}
        data['client_id'] = settings.FACEBOOK_APP_ID
        data['redirect_uri'] = "http://localhost:8000/animal/facebook_login"
        data['client_secret'] = settings.FACEBOOK_API_SECRET
        data['code'] = request.GET['code']
        data = urllib.urlencode(data)
        req = urllib2.Request(url, data)
        print req
        response = urllib2.urlopen(req)
        html = response.read()
        res = html.split("&")
        access_token = res[0].replace("access_token=","")
    except HTTPError as e:
        return HttpResponse("Get access token error: " + e.reason)
    #get app_token
    url = "https://graph.facebook.com/oauth/access_token"
    data = {}
    data['client_id'] = settings.FACEBOOK_APP_ID
    data['client_secret'] = settings.FACEBOOK_API_SECRET
    data['grant_type'] = "client_credentials"
    data = urllib.urlencode(data)
    print req
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    html = response.read()
    app_token = html.replace("access_token=","")
    print app_token
    #get debug token
    url = "https://graph.facebook.com/debug_token"
    data = {}
    data['input_token'] = access_token
    data['access_token'] = app_token
    data = urllib.urlencode(data)
    req = "%s?%s" % (url , data)
    print req
    response = urllib2.urlopen(req)
    html = response.read()
    return HttpResponse(html)

def register(request):
      return render_to_response('register.html',
              context_instance=RequestContext(request))

#TODO: use view get image
def get_img(request):
    pass
