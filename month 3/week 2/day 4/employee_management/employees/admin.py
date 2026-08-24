from django.contrib import admin
from .models import Employees,Project,Department,EmployeeProfile
# Register your models here.

admin.site.register(Employees) 
admin.site.register(Project) 
admin.site.register(Department) 
class DepartmentAdmin(admin.ModelAdmin):
    list_display={
        "id","name","code"
    }
    
admin.site.register(EmployeeProfile) 