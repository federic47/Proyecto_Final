from django import forms

class CompuFormularios(forms.Form):
    #Especificamos el formulario 
    fabricante = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)

class ProcesadorFormularios(forms.Form):
    #Especificamos el formulario 
    fabricante = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)

class MotherboardFormularios(forms.Form):
    #Especificamos el formulario 
    fabricante = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)
