from django.shortcuts import render_to_response
from models import Animal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    animals = Animal.objects.order_by("-id")
    paginator = Paginator(animals, 10)
    animals = paginator.page(1)
    print animals

    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]

    return render_to_response('index.html', {"animals": animals} )

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
      return render_to_response('login.html')

#TODO: use view get image
def get_img(request):
    pass