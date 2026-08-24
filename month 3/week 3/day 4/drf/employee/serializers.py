from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
   class Meta:
     model = Employee
     fields = '__all__'

     read_only_fields = [
        "id","created_at",
     ]

     def validate_age(self,value):
        if value < 18:
           raise serializers.ValidationError("Employee must be at least 18 years old.")
        if value > 65:
              raise serializers.ValidationError("Employee can not be geater than  65. ")

     def validate(self, attrs):
        if(attrs.get("department") == "HR" and attrs.get("Salary",0) < 20000):
            raise serializers.ValidationError("HR Employee must have salary of at least 20000")

        return attrs
                   
           
#1. field-level validation: specific field
#2. object-level validation: when validations required multiple field