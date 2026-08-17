from django.urls import path
from students.views import home,contact,about

urlpatterns = [
    path('home', home,name="home"),
    path('contact', contact,name="contact"),
    path('about', about,name="about"),
]
