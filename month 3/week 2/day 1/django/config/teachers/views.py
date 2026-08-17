from django.shortcuts import render
from django.http import HttpResponse #returns response to browser

def home(request):
    return HttpResponse("home page of teacher!")
def contact(request):
    return HttpResponse("contact teacher!")
def about(request):
    return HttpResponse("teachers are of this school !")