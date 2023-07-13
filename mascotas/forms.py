from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre','descripcion', 'precio', 'stock', 'imagen', 'categoria']
        labels = {
            'codigo' : 'Codigo',
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
            'precio' : 'Precio',
            'stock' : 'Stock',
            'imagen' : 'Imagen',
            'categoria' : 'Categoria',
        }
        widgets = {
            'codigo' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingrese el codigo',
                    'class' : 'form-control',
                    'id' : 'codigo'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingrese el nombre',
                    'class' : 'form-control',
                    'id' : 'nombre'
                }
            ),
            'descripcion' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingrese una descripcion',
                    'class' : 'form-control',
                    'id' : 'descripcion'
                }
            ),
            'precio' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingrese el precio',
                    'class' : 'form-control',
                    'id' : 'precio'
                }
            ),
            'stock' : forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingrese el stock',
                    'class' : 'form-control',
                    'id' : 'stock'
                }
            ),
            'imagen' : forms.FileInput(
                attrs = {
                    'class' : 'form-control',
                    'id' : 'codigo'
                }
            ),
            'categoria' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'id' : 'codigo'
                }
            ),
        }