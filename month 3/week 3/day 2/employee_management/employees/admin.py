from django.contrib import admin
from .models import Employees,Project,Department,EmployeeProfile
# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'dept_name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'proj_name', 'start_date', 'is_completed']


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'age',
        'city',
        'branch',
        'is_active',
        'created_at',
        'proj_name',
        'dept_name',
    ]


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'employee',
        'bio',
        'phone',
        'address',
    ]