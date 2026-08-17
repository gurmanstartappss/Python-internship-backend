from django.urls import path
from students.views import home,contact,about,students_details

urlpatterns = [
    path('home', home,name="home"),
    path('contact', contact,name="contact"),
    path('about', about,name="about"),
    path('<int:students_id>/',students_details,name="students_details")
    
]
