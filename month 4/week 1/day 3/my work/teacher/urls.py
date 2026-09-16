from django.urls import path
from .views import Home

urlpatterns = [
    path('home/<int:id>',Home.as_view()),
]
