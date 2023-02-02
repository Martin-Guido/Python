from django.shortcuts import render
from  carro.carro import Carro 
from tienda.models import producto as Producto
from django.shortcuts import redirect

def agregar_producto(request,producto_id):
	carro=Carro(request)
	producto=Producto.objects.get(id=producto_id)
	carro.agregar(producto=producto)

	return redirect('tienda')


def eliminar_producto(request,producto_id):
	carro=Carro(request)
	producto=Producto.objects.get(id=producto_id)
	carro.eliminar(producto=producto)

	return redirect('tienda')



def restar_producto(request,producto_id):
	carro=Carro(request)
	producto=Producto.objects.get(id=producto_id)
	carro.restar(producto=producto)

	return redirect('tienda')
# Create your views here.

def limpiar(request,producto_id):
	carro=Carro(request)
	
	carro.limpiar_carro()

	return redirect('tienda')
