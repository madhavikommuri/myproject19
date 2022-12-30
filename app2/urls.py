from django.urls import path
from app1.views import *

app_name='nature'

urlpatterns=[
    path('environment/', environment,name='environment'),
]