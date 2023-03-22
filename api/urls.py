from django.urls import path
from .views import *

urlpatterns = [
    path("",index, name="index"),
    path("signup/",signup,name="signup"),
    path("login/",logIn, name="login"),
    path("logout/",logOut, name="logout"),
    path("login/cv/",cv,name="cvpeople"),
    path("cvform/",cvform,name="cvform"),
    path("cvform/cv",cv,name="cv")
    
]


