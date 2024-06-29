from django.shortcuts import render
from .models import Producto, Proveedor, Pedido

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

