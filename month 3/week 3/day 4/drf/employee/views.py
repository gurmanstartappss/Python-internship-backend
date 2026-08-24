from django.shortcuts import render

from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import AllowAny
from .throttles import EmployeeRateThrottle

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]
    throttle_classes = [EmployeeRateThrottle]



#viewset: viewset is a class that groups 
# related API operations such as list,create,retrieve,update,delete into a single class

#Router: router autometically generated URL patterns for viewSets.

