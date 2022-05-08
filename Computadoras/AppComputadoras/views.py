from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from AppComputadoras.forms import CompuFormularios,ProcesadorFormularios,MotherboardFormularios

#---------------------------------------------------------------------------------------
def computadora(request):

     #-------SI entra por Post cuando viene un formulario cargado--------
    if request.method =='POST':
         #Crea una variable  donde llama a la clase forms de Forumulario 
         miFormulario = CompuFormularios(request.POST)

         #Pregunta si el formulario que este todo  ok  es decir datos validos
         if miFormulario.is_valid():
              #crea variable informacion y limpia con metodo
              informacion = miFormulario.cleaned_data
              #Asigna esos datos limpiados a la creacion de las compus con esos parametros
              computadora = Computadora(fabricante=informacion['fabricante'], marca=informacion['marca'])
              computadora.save()
              return render(request, 'AppComputadoras/inicio.html')
    else:
          miFormulario = CompuFormularios()
    return render(request, 'AppComputadoras/computadoras.html' , {'formulario': miFormulario})
#-----------------------------------------------------------------------------------------------------

def busquedaMarca(request):
     return render(request, 'AppComputadoras/busquedaMarca.html')
    

def buscar(request):
     
    if request.GET['marca']:
         marca = request.GET['marca']
         computadoras = Computadora.objects.filter(fabricante=marca)

         return render(request,'AppComputadoras/resultadosBusqueda.html', {'computadoras': computadoras, 'marca':marca})
    else:
          repuesta = "No se ingreso datos de ninguna Computadora"
          return render(request, 'AppComputadoras/resultadosBusqueda.html',{'repuesta': repuesta})


#--------Definimos la views de inicio------------------#
def inicio(request):
    return render(request,'AppComputadoras/inicio.html')


#-----------Definimos la views de Procesador------#
def procesador(request):
      #-------SI entra por Post cuando viene un formulario cargado--------
    if request.method =='POST':
         #Crea una variable  donde llama a la clase forms de Forumulario 
         miProcesador= ProcesadorFormularios(request.POST)

         #Pregunta si el formulario que este todo  ok  es decir datos validos
         if miProcesador.is_valid():
              #crea variable informacion y limpia con metodo
              informacion = miProcesador.cleaned_data
              #Asigna esos datos limpiados a la creacion de las compus con esos parametros
              procesador = Procesador(nombre=informacion['fabricante'], numeroModelo=informacion['marca'])
              procesador.save()
              return render(request, 'AppComputadoras/inicio.html')
    else:
         miProcesador = ProcesadorFormularios()
    return render(request, 'AppComputadoras/procesador.html' , {'formulario': miProcesador})

#-----------Definimos la views de Procesador------#
def motherboard(request):
       #-------SI entra por Post cuando viene un formulario cargado--------
    if request.method =='POST':
         #Crea una variable  donde llama a la clase forms de Forumulario 
         miMotherboard= MotherboardFormularios(request.POST)

         #Pregunta si el formulario que este todo  ok  es decir datos validos
         if miMotherboard.is_valid():
              #crea variable informacion y limpia con metodo
              informacion = miMotherboard.cleaned_data
              #Asigna esos datos limpiados a la creacion de las compus con esos parametros
              motherboard = Motherboard(marca=informacion['fabricante'], modelo=informacion['marca'])
              motherboard.save()
              return render(request, 'AppComputadoras/inicio.html')
    else:
         miMotherboard = MotherboardFormularios()
    return render(request, 'AppComputadoras/motherboard.html' , {'formulario': miMotherboard})