from django.shortcuts import render, redirect
from .models import Producto, Boleta, detalle_boleta
from .forms import ProductoForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from mascotas.compra import Carrito

# Create your views here.

def index(request):

    return render(request, 'Inicio.html')

def mision(request):
    return render(request, 'Mision.html')

def productos(request):
    productos = Producto.objects.all()
    elementos_por_pagina = 10
    paginator = Paginator(productos, elementos_por_pagina)
    page = request.GET.get('page')
    productos_paginados = paginator.get_page(page)
    datos={'productos': productos_paginados}
    return render(request, 'Productos.html', datos)

def voluntariado(request):

    return render(request, 'Voluntariado.html')

def listaVoluntarios(request):

    return render(request, 'ListaVoluntarios.html')

@login_required
def registroStock(request):
    productos=Producto.objects.all()
    datos={'productos' : productos}
    return render(request, 'registroStock.html', datos)

@login_required
def ingresarProducto(request):
    if request.method=="POST":
        productoform = ProductoForm(request.POST, request.FILES)
        if productoform.is_valid():
            productoform.save()
            return redirect('registroStock')
    else:
        productoform=ProductoForm()
    return render (request, 'ingresarProducto.html', {'productoform' : productoform})

@login_required
def eliminarProducto(request,id):
    productoEliminado = Producto.objects.get(codigo=id)
    productoEliminado.delete()
    return redirect('registroStock')

@login_required
def modificarProducto(request,id):
    productoModificado = Producto.objects.get(codigo=id)
    datos = {
        'form' : ProductoForm(instance=productoModificado)
    }
    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('registroStock')
    return render(request, 'modificarProducto.html', datos)

def registrar(request):
    data={
        'form' : RegistroUserForm()
    }
    if request.method=="POST":
        formulario=RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
        data["form"]=formulario
    return render(request, 'registration/registrar.html', data)

def carrito(request):

    return render(request, 'carrito.html')

#Compra / administracion carrito

@login_required
def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.agregar(producto=producto)
    return redirect('productos')

def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('carrito')

def restar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.restar(producto=producto)
    return redirect('carrito')

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('carrito')

#
def detalle_carrito(request):
    return render(request,'detallecarrito.html')

def generarBoleta(request):
    precio_total = 0
    subtotal = 0
    username=""     
    estado=""
    for key, value in request.session['carrito'].items():
        username = request.user.username
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
        subtotal = 0
        estado= "Procesando Pedido"  
        boleta = Boleta(total = precio_total)
        boleta.save()
        productos = []

    for key, value in request.session['carrito'].items():
        producto = Producto.objects.get(codigo = value['producto_id'])
        cant = value['cantidad']

        if producto.stock >= cant :
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
        
            producto.stock -= cant
            producto.save()

    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total':boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    carrito = Carrito(request, 'detallecarrito.html', datos)
            