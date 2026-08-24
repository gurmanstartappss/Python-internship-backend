"""
query look up
age__gt=18
__lt
__lte

if i want to search gurman
name_icontains="gurman"

code:- in views.py
Student.objects.filter(name__icontains="gurman")
Student.objects.order_by("-age").first()
Student.objects.order_by("-age").last()
Student.objects.filter(email="gurman").exists()

Count():-
Student.objects.count()
Student.objects.filter(email="gurman").count()

values():-
Student.objects.values("name","email")

"""