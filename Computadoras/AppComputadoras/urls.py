from django.urls import path

from .views import *

urlpatterns = [
    path('',inicio,name='inicio'),
    path('procesador/', procesador, name='procesador'),
    path('motherboard/',  motherboard, name='motherboard'),
]