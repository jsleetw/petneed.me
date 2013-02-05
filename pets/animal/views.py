from django.shortcuts import render_to_response
from models import Animal

def home(request):
    animals = Animal.objects.order_by("-id")[:30]
    animals.reverse()
    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]

    return render_to_response('index.html', {"animals": animals} )

#TODO: use view get image
def get_img(request):
    pass
