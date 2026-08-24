from django.db import models


# Create your models here.
class EmployeeQuerySet(models.QuerySet):

    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)

    def adults(self):
        return self.filter(age__gte=18)
    
class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dept_name


class Project(models.Model):
    proj_name = models.CharField(max_length=100)
    start_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.proj_name


class Employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    proj_name = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    dept_name = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    objects = EmployeeQuerySet.as_manager()

    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):
    employee = models.OneToOneField(
        Employees,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.employee.name
    
    
