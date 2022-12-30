from django.urls import path
from app1.views import *

app_name='madhu'

urlpatterns=[
    path('world/',world,name='world')
]