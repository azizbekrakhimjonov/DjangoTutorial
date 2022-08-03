from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Members


# def index(request):
#     return HttpResponse("Hello world!")


# def index(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())


# def index(request):
#     mymembers = Members.objects.all().values()
#     output = ""
#     for x in mymembers:
#         output += x["firstname"]
#     return HttpResponse(output)



# def index(request):
#   mymembers = Members.objects.all().values()
#   template = loader.get_template('index.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))


# def index(request):
#   mymembers = Members.objects.all().values()
#   template = loader.get_template('index.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))
#
#
# def add(request):
#   template = loader.get_template('add.html')
#   return HttpResponse(template.render({}, request))


def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))