from django.urls import path,include
from .views import About,employees_create,Contact,List,Home,employees_list

urlpatterns = [
    
    path('About/',About,name="About"),
    path('Contact/',Contact,name="Contact"),
    path('List/',List,name="List"),
    path('employees_list/',employees_list,name="employees_list"),
    path('create/',employees_create,name="create"),
     path('accounts/', include('accounts.urls')),
]
