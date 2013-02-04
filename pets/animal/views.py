from django.shortcuts import render_to_response
from models import Animal

def home(request):

    d = []
    animals = Animal.objects.all()[:10]

    return render_to_response('index.html', {"animals": animals} )

#TODO: use view get image
def get_img(request):
    pass
