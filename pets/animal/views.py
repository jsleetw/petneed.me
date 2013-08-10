from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Animal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.utils import simplejson

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
    animals = Animal.objects.order_by("-id")
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
                                    'note': animal.note,
                                    'resettlement': animal.resettlement,
                                    'phone': animal.phone,
                                    'email': animal.email,
                                    'childre_anlong': animal.childre_anlong,
                                    'animal_anlong': animal.animal_anlong,
                                    'bodyweight': animal.bodyweight,
                                    'image_name': animal.image_name,
                                    'image_file': animal.image_file,
                                    'pub_date': animal.pub_date.strftime("%B %d, %Y") } 
                                        for animal in animals] )
    # print json.decode("unicode_escape")
    return HttpResponse(json.decode("unicode_escape"), mimetype="application/json")

#TODO: use view get image
def get_img(request):
    pass
