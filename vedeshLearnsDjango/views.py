# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request, 'website/index.html')

def home(request):
  # return HttpResponse("Hello, World! This is Vedesh's HomePage")
  return render(request, 'website/home.html')

def about(request):
  # return HttpResponse("I am a student")
  return render(request, 'website/about.html')


def contact(request):
  # return HttpResponse("You can reach me at vpadal04@gmail.com")
  return render(request, 'website/contact.html')


