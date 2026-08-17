from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()
    city=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.name