from django.db import models


class Employee(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField(unique=True)
     age = models.PositiveIntegerField()
     department = models.CharField(max_length=50)
     salary = models.DecimalField(max_digits=10,decimal_places=2)
     is_active = models.BooleanField(default=True)
     created_at = models.DateTimeField(auto_now_add=True)

#basic authentication/jwt authe /third party uthentication/ session authentication



