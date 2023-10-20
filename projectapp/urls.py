from django.urls import path
from projectapp.views import salom

urlpatterns =[
    path('',salom,name="index")
]