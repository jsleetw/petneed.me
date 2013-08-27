import json
import pprint
import urllib
import urllib2
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Animal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.utils import simplejson
from urllib2 import HTTPError
from django.http import HttpResponse
from django.conf import settings
from animal.models import User

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

def get_animals(request):
    animals = Animal.objects.order_by('-id')
    if request.GET.get('limit'):
        limit_num = int(request.GET.get('limit'))
        pages = Paginator(animals, limit_num)
        if request.GET.get('page'):
            page_num = request.GET.get('page')
            animals = pages.page(page_num)
        else:
            animals = pages.page(1)
    json = simplejson.dumps([{'accept_num': animal.accept_num,
                                    'name': animal.name,
                                    'sex': animal.sex,
                                    'type': animal.type,
                                    'build': animal.build,
                                    'age': animal.age,
                                    'variety': animal.variety,
                                    'reason': animal.reason,
                                    'chip_num': animal.chip_num,
                                    'is_sterilization': animal.is_sterilization,
                                    'hair_type': animal.hair_type,
                                    'note': animal.note.replace('"', '\\"'),
                                    'resettlement': animal.resettlement,
                                    'phone': animal.phone,
                                    'email': animal.email,
                                    'childre_anlong': animal.childre_anlong,
                                    'animal_anlong': animal.animal_anlong,
                                    'bodyweight': animal.bodyweight,
                                    'image_name': animal.image_name,
                                    'image_file': animal.image_file,
                                    'pub_date': animal.pub_date.strftime('%B %d, %Y') } 
                                        for animal in animals] )
    # print json.decode("unicode_escape")
    return HttpResponse(json.decode('unicode_escape'), mimetype='application/json')

def get_specific_animal(request, accept_num):
    animal = Animal.objects.filter(accept_num = accept_num)
    print animal
    if len(animal) > 0:
        animal = animal[0]
    else:
        return HttpResponse(status=404, mimetype='application/json')
    json = simplejson.dumps({'accept_num': animal.accept_num,
                                    'name': animal.name,
                                    'sex': animal.sex,
                                    'type': animal.type,
                                    'build': animal.build,
                                    'age': animal.age,
                                    'variety': animal.variety,
                                    'reason': animal.reason,
                                    'chip_num': animal.chip_num,
                                    'is_sterilization': animal.is_sterilization,
                                    'hair_type': animal.hair_type,
                                    'note': animal.note,
                                    'resettlement': animal.resettlement,
                                    'phone': animal.phone,
                                    'email': animal.email,
                                    'childre_anlong': animal.childre_anlong,
                                    'animal_anlong': animal.animal_anlong,
                                    'bodyweight': animal.bodyweight,
                                    'image_name': animal.image_name,
                                    'image_file': animal.image_file,
                                    'pub_date': animal.pub_date.strftime('%B %d, %Y') })
    return HttpResponse(json.decode('unicode_escape'), mimetype='application/json')

def __get_access_token(request):
    url = "https://graph.facebook.com/oauth/access_token"
    data = {}
    data['client_id'] = settings.FACEBOOK_APP_ID
    data['redirect_uri'] = "http://localhost:8000/animal/facebook_login"
    data['client_secret'] = settings.FACEBOOK_API_SECRET
    data['code'] = request.GET['code']
    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    html = response.read()
    res = html.split("&")
    access_token = res[0].replace("access_token=","")
    return access_token

def __get_app_token(request):
    url = "https://graph.facebook.com/oauth/access_token"
    data = {}
    data['client_id'] = settings.FACEBOOK_APP_ID
    data['client_secret'] = settings.FACEBOOK_API_SECRET
    data['grant_type'] = "client_credentials"
    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    html = response.read()
    app_token = html.replace("access_token=","")
    return app_token

def __get_debug_json(request, access_token, app_token):
    url = "https://graph.facebook.com/debug_token"
    data = {}
    data['input_token'] = access_token
    data['access_token'] = app_token
    data = urllib.urlencode(data)
    req = "%s?%s" % (url , data)
    response = urllib2.urlopen(req)
    return response.read()

def facebook_login(request):
    access_token = __get_access_token(request)
    print "access_token:" + str(access_token)
    app_token = __get_app_token(request)
    print "app_token:" + str(app_token)
    debug_json = __get_debug_json(request, access_token, app_token)
    print "debug_json:" + str(debug_json)

    debug_json_obj = json.loads(str(debug_json))
    fb_user_id = debug_json_obj["data"]["user_id"]
    f = User.objects.filter(fb_user_id=fb_user_id)
    pprint.pprint(f)
    if not f:
        print "no data in User"
    #TODO:@jslee:check token and update last_login_date
    return HttpResponse(debug_json)

def register(request):
    return render_to_response('register.html',
            context_instance=RequestContext(request))

#TODO@jslee: use view get image
def get_img(request):
    pass
