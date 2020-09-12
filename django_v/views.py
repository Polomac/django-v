from django.http import HttpResponse;
from django.shortcuts import render;

def home(request):
  # return HttpResponse('<div><h1>HOMEPAGE</h1></div>')
  return render(request, 'home.html')

def about(request):
  # return HttpResponse('<div><h1>ABOUT</h1></div>')
  return render(request, 'about.html')