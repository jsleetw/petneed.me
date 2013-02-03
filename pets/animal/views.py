from django.shortcuts import render_to_response

def home(request):

    d = {}

    return render_to_response('home.html', d)
