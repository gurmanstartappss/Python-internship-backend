from django.shortcuts import render,redirect
from .models import Employees
from .forms import EmployeesForm
# Create your views here.
def Home(request):
    return render(request,"employees/Home.html")             

def About(request):
    context={
        "emp_name":"Gurman",
        "dept_name":"Python Developer",
        "age":"23",
        "branch":"IT",
        "city":"Indore",
    }
    return render(request,"employees/About.html",context)

def Contact(request):
    context={
        "emp_name":"Gurman",
        "dept_name":"Python Developer",
        "contact":"xxxxxxxx52",
        "email":"xxxx@gmail.com",
        "address":"sahara city homes 452016",
    }
    return render(request,"employees/Contact.html",context)

def List(request):
    employees={"gurman":900000,"avantika":110000,"druv":30000,"vivek":20000,"nitesh":70000}
    context = {"employees":employees}
    return render(request,"employees/List.html",context)   

def employees_list(request):
    employees = Employees.objects.values()
    return render(request, "employees/employees_list.html", {"employees": employees})


def employees_create(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        city=request.POST.get("city")
        age=request.POST.get("age")
        branch=request.POST.get("branch")
        
        Employees.objects.create(name = name, email=email, city=city, age=age, branch=branch)
        return redirect("employees_list")
    return render(request,"employees/employees_create.html")

def employee_create(request):
    if request.method == "POST":
        form = EmployeesForm(request.POST)

        if form.is_valid():
            employee = form.save()
            return redirect("employee-detail", pk=employee.pk)

    else:
        form = EmployeesForm()

    return render(request, "employee_create.html", {"form": form})