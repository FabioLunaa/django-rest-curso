""" from django.shortcuts import render
from mascotar_app.models import Producto
from django.http import JsonResponse

def producto_list(request):
    productos = Producto.objects.all()
    data = {
        'productos': list(productos.values()),
    }
    return JsonResponse(data)

def producto_detalle(request, pk):
    producto = Producto.objects.get(pk=pk)
    data = {
        'imagen': producto.linkImagen,
        'descripcion': producto.descripcion,
    }
    return JsonResponse(data) """