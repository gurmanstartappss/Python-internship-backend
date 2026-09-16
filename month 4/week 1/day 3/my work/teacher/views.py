from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 

# Create your views here.

class Home(View):
    def get(self,request,id):
        return HttpResponse(f"hello teacher {id}")
    
    def post(self,request):
            return HttpResponse("hello")