from django.shortcuts import render_to_response
from models import Animal

def home(request):

    animals = Animal.objects.all()[:10]
    for i in animals:
        i.smal_img_file = "%s_248x350.jpg" % i.image_file.split(".jpg")[0]

    return render_to_response('index.html', {"animals": animals} )

#TODO: use view get image
def get_img(request):
    pass
