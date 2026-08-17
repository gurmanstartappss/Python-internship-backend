from django.shortcuts import render
from django.http import HttpResponse #returns response to browser
from django.shortcuts import render

def home(request):
    students=[
        "name","abc",
        "course","django"
    ]
    return render(request,"students/home.html",{"students":students})
def contact(request):
    return HttpResponse("contact students !")
def about(request):
    return HttpResponse("students of this school !")

def students_details(request,students_id):
    return HttpResponse(f"Student ID:{students_id}")
