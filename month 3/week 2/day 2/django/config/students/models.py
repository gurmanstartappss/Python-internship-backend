from django.db import models

# Create your models here.
class Student (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()
    city=models.CharField(max_length=100)
    course=models.CharField(max_length=100,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
"""in terminal
>>> from students.models import Student
>>> student=Student.objects.create(name="abc",email="abc@gmail.com",age=22,city="indore",course="btech")
>>> std=Student.objects.all()
>>> print(std)  

"""