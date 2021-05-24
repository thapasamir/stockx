from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("service", views.service, name="service"),
    path("news", views.news, name="news"),
    #tools
    path("costcalculator", views.costcal, name="costcal"),


    

]
