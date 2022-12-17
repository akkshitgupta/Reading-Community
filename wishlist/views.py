from django.shortcuts import render
from django.http import HttpRequest
from django.template import loader
# Create your views here.

def show(request):
    template = loader.get_template('show.html')  
    return HttpRequest(template.render({},request))


# def reset(request):
#     return HttpRequest('<h1>Its show time baby</h1>')