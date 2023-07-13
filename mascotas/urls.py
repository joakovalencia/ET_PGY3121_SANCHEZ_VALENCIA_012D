from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name="index"),
    path('mision/', mision, name="mision"),
    path('productos/', productos, name="productos"),
    path('voluntariado/', voluntariado, name="voluntariado"),
    path('listaVoluntarios/', listaVoluntarios, name="listaVoluntarios"),
    path('registroStock/', registroStock, name="registroStock"),
    path('ingresarProducto/', ingresarProducto, name="ingresarProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    path('registrar/', registrar, name="registrar"),
    path('carrito/', carrito, name="carrito"),

    path('generarBoleta/', generarBoleta, name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('detalle_carrito/' , detalle_carrito, name="detalle_carrito"),
]