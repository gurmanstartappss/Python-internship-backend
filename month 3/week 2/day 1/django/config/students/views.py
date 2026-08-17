from django.shortcuts import render
from django.http import HttpResponse #returns response to browser

def home(request):
    return HttpResponse("Hello students!")
def contact(request):
    return HttpResponse("contact students !")
def about(request):
    return HttpResponse("students of this school !")

#get, post, header, cookies, user, query , body