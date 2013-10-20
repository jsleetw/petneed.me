# coding: utf-8

import re
import os
import json
import urllib
import urllib2
import time
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
#from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator
from django.template import RequestContext
from django.utils import simplejson
from django.conf import settings
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user
from models import Animal, FindAnimal
from django.contrib.auth import get_user_model
from animal.utils import thumbnail
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from animal.models import LostAnimal
from animal.forms import LostAnimalForm

class LostAnimalCreate(CreateView):
    model = LostAnimal
    form_class = LostAnimalForm
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(LostAnimalCreate, self).form_valid(form)

class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=20)
    conf_password = forms.CharField(max_length=20)

class UploadForm(forms.Form):
    name = forms.CharField(max_length=200)
    #sex = forms.CharField(max_length=200)
    #type = forms.CharField(max_length=200)
    #build = forms.CharField(max_length=200)
    #age = forms.CharField(max_length=200)
    #variety = forms.CharField(max_length=200)
    #reason = forms.CharField(max_length=200)
    #accept_num = forms.CharField(max_length=200)
    #chip_num = forms.CharField(max_length=200)
    #is_sterilization = forms.CharField(max_length=200)
    #hair_type = forms.CharField(max_length=200)
    note = forms.CharField()
    resettlement = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=200)
    #email = forms.EmailField()
    #childre_anlong = forms.CharField(max_length=200)
    #animal_anlong = forms.CharField(max_length=200)
    #bodyweight = forms.CharField(max_length=200)
    photo = forms.ImageField()

def home(request):
    animals = Animal.objects.order_by("-id")
    paginator = Paginator(animals, 10)
    animals = paginator.page(1)
    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]
    return render_to_response('index.html', {"animals": map(__extend_animal_fields,animals)}, context_instance=RequestContext(request))


def page(request):
    page = int(request.path_info.strip('/animal/page/'))
    animals = Animal.objects.order_by("-id")
    paginator = Paginator(animals, 10)
    animals = paginator.page(page)
    print animals
    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]
    return render_to_response('page.html', {"animals": map(__extend_animal_fields,animals)})


def profile(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    animal = __extend_animal_fields(animal)
    return render_to_response('profile.html', {'current_url':
                              'http://petneed.me' + request.get_full_path(), "animal": animal},
                              context_instance=RequestContext(request))


def __extend_animal_fields(animal):
    animal.sex_class = 'male' if unicode(animal.sex) == u'雄' else 'female'
    animal.smal_img_file = "%s_248x350.jpg" % animal.image_file.split(".jpg")[0]
    animal.phone_normalized = re.sub('[ ()-]', '', animal.phone)  # used in tel:// protocol

    shared_target = {'u': 'http://%s/animal/profile/%s' % (settings.SITE_DOMAIN, animal.id)}
    shared_target = urllib.urlencode(shared_target)
    animal.share_link_facebook = 'http://www.facebook.com/sharer/sharer.php?u=' + shared_target

    # higher (integer) score reflects that the animal is more close to children/animal
    # zero as strong negative
    animal.children_score = __calculate_children_score(animal.childre_anlong)
    animal.animal_score = __calculate_animal_score(animal.animal_anlong)

    return animal

def __calculate_children_score(statement):
    score = 0
    if u'可' == statement:
        score = 3
    elif u'可' in statement:
        score = 2
    elif u'不建議' in statement:
        score = 1
    elif u'不可' in statement:
        score = 0
    return score

def __calculate_animal_score(statement):
    score = 0
    if u'可' in statement:
        score = 1
    elif u'不可' in statement:
        score = 0
    return score

def user_profile(request):
    user = get_user(request)
    print user
    return render_to_response("user_profile.html", context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        print user.is_active
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                print "login success"
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('1')
                # Return a 'disabled account' error message
        else:
            return HttpResponse('2')
            # Return an 'invalid login' error message.
    return render_to_response('login.html', context_instance=RequestContext(request))


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
    api_json = simplejson.dumps([{'accept_num': animal.accept_num,
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
                                  'pub_date': animal.pub_date.strftime('%B %d, %Y')} for animal in animals])
    # print json.decode("unicode_escape")
    return HttpResponse(api_json.decode('unicode_escape'), mimetype='application/json')


def get_specific_animal(request, accept_num):
    animal = Animal.objects.filter(accept_num=accept_num)
    if len(animal) > 0:
        animal = animal[0]
    else:
        return HttpResponse(status=404, mimetype='application/json')
    api_json = simplejson.dumps({'accept_num': animal.accept_num,
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
                                 'pub_date': animal.pub_date.strftime('%B %d, %Y')})
    return HttpResponse(api_json.decode('unicode_escape'), mimetype='application/json')


def __get_access_token(request):
    url = "https://graph.facebook.com/oauth/access_token"
    data = {}
    data['client_id'] = settings.FACEBOOK_APP_ID
    data['redirect_uri'] = "http://localhost:8000/animal/facebook_register"
    data['client_secret'] = settings.FACEBOOK_API_SECRET
    data['code'] = request.GET['code']
    data = urllib.urlencode(data)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    html = response.read()
    res = html.split("&")
    access_token = res[0].replace("access_token=", "")
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
    app_token = html.replace("access_token=", "")
    return app_token


def __get_debug_json(request, access_token, app_token):
    url = "https://graph.facebook.com/debug_token"
    data = {}
    data['input_token'] = access_token
    data['access_token'] = app_token
    data = urllib.urlencode(data)
    req = "%s?%s" % (url, data)
    response = urllib2.urlopen(req)
    return response.read()


def __get_fb_email(request, access_token):
    url = "https://graph.facebook.com/fql"
    data = {}
    data['q'] = "SELECT email FROM user WHERE uid=me()"
    data['access_token'] = access_token
    data = urllib.urlencode(data)
    req = "%s?%s" % (url, data)
    response = urllib2.urlopen(req)
    return response.read()


def facebook_register(request):
    access_token = __get_access_token(request)
    print "access_token:" + str(access_token)
    app_token = __get_app_token(request)
    print "app_token:" + str(app_token)
    debug_json = __get_debug_json(request, access_token, app_token)
    print "debug_json:" + str(debug_json)
    debug_json_obj = json.loads(str(debug_json))
    fb_user_id = debug_json_obj["data"]["user_id"]
    print fb_user_id
    email_json = __get_fb_email(request, access_token)
    email_json_obj = json.loads(str(email_json))
    email = email_json_obj["data"][0]["email"]
    print "fb_mail:" + email
    User = get_user_model()
    f = User.objects.filter(email=email)
    if not f:
        pass
    return HttpResponse("hi")


def facebook_login(request):
    access_token = __get_access_token(request)
    print "access_token:" + str(access_token)
    app_token = __get_app_token(request)
    print "app_token:" + str(app_token)
    debug_json = __get_debug_json(request, access_token, app_token)
    print "debug_json:" + str(debug_json)
    debug_json_obj = json.loads(str(debug_json))
    fb_user_id = debug_json_obj["data"]["user_id"]
    User = get_user_model()
    f = User.objects.filter(fb_user_id=fb_user_id)
    if not f:
        #init new user data
        u = User(email="unknow",
                 is_fb=True,
                 fb_access_token=access_token,
                 fb_user_id=fb_user_id)
        u.save()
    else:
        #update access_token and last_login_date
        f.access_token = access_token
        f.last_login_date = datetime.now()
        print f.last_login_date
        f.save()
    #redirect back to front page
    return HttpResponseRedirect('/animal/login/')


def register(request):
    error_msg = False
    User = get_user_model()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            conf_password = request.POST.get("conf_password")
            if not password == conf_password:
                error_msg = "password not equal"
            else:
                u = User.objects.filter(email=email)
                if not u:
                    user = User.objects.create_user(email, password)
                    user.save()
                    return HttpResponseRedirect('/animal/thanks')
                else:
                    print "user is exist"
                    error_msg = "user is exist"
        else:
            print "invalided"
            error_msg = form.errors
    return render_to_response('register.html', {'error_msg': error_msg}, context_instance=RequestContext(request))


def thanks(request):
    return render_to_response('thanks.html', context_instance=RequestContext(request))

def upload(request):
    error_msg = False
    user = get_user(request)
    if request.method == 'POST':
        if not user.is_authenticated():
            return HttpResponseRedirect("/")
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            a = Animal() 
            a.name = request.POST.get("name")
    	    #a.sex = request.POST.get("sex")
            #a.type = request.POST.get("type")
            #a.build = request.POST.get("build")
            #a.age = request.POST.get("age")
            #a.variety = request.POST.get("variety")
            #a.reason = request.POST.get("reason")
            #a.accept_num = request.POST.get("accept_num")
            #a.chip_num = request.POST.get("chip_num")
            #a.is_sterilization = request.POST.get("is_sterilization")
            #a.hair_type = request.POST.get("hair_type")
            a.note = request.POST.get("note")
            a.resettlement = request.POST.get("resettlement")
            a.phone = request.POST.get("phone")
            #a.email = request.POST.get("email")
            #a.childre_anlong = request.POST.get("childre_anlong")
            #a.nimal_anlong = request.POST.get("animal_anlong")
            #a.bodyweight = request.POST.get("bodyweight")
            image = request.FILES['photo']
            
            head, ext = os.path.splitext(image.name)
            filename = user.get_username() + str(int(time.time())) + ext
            savefilename = "src/media/" + filename
            # TODO : try-catch for PIL errors
            with open(savefilename, "wb") as code:
                code.write(image.read())
            a.image_file = filename
            thumbnail(savefilename, "248x350")
            thumbnail(savefilename, "248x350", True)
            a.save()
            # TODO : return new page while upload success
            return HttpResponseRedirect("/")
        else:
            print "invalided"
            print form.errors
            return render_to_response('upload.html', {'error_msg': form.errors}, context_instance=RequestContext(request))
    return render_to_response('upload.html', context_instance=RequestContext(request))

#TODO@jsleetw: use view get image
def get_img(request):
    pass


def find_animal_upload(request):
    return render_to_response('find_animal_upload.html', context_instance=RequestContext(request))


def find_animal(request):
    animals = FindAnimal.objects.order_by("-id")
    paginator = Paginator(animals, 10)
    animals = paginator.page(1)
    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]
    return render_to_response('find_animal.html', {"animals": animals}, context_instance=RequestContext(request))


def find_animal_page(request, page_num):
    animals = FindAnimal.objects.order_by("-id")
    paginator = Paginator(animals, 10)
    try:
        animals = paginator.page(page_num)
    except:
        return HttpResponseNotFound()

    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]
    return render_to_response('page.html', {"animals": animals})

