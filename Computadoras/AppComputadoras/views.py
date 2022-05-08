from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from AppComputadoras.forms import CompuFormularios

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
     return render(request,'AppComputadoras/procesador.html')

#-----------Definimos la views de Procesador------#
def motherboard(request):
     return render(request,'AppComputadoras/motherboard.html')