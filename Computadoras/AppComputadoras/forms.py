from django import forms

class CompuFormularios(forms.Form):
    #Especificamos el formulario 
    fabricante = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50)
