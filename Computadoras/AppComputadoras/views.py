from django.shortcuts import render
from .models import *




#--------Definimos la pagina de inicio----------#
def inicio(request):
    return render(request,'AppComputadoras/inicio.html')

#-----------Definimos la views de Procesador------#
def procesador(request):
     return render(request,'AppComputadoras/procesador.html')

#-----------Definimos la views de Procesador------#
def motherboard(request):
     return render(request,'AppComputadoras/motherboard.html')