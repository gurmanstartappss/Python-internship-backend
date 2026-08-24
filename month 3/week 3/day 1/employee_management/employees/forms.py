from django import forms
from .models import Department,Project,Employees,EmployeeProfile

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields = "__all__" #takes all fields from models
        
        # for custom input way like for eg forms 
        widgets={
            "department":forms.CheckboxSelectMultiple
        }