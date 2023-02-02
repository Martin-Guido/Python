from django.shortcuts import render
from .models import categoriaprod as cat_id,producto as prd
#from carro.carro import Carro
# Create your views here.
def tienda(request):

	
	

	productos=prd.objects.all()

	return  render(request,'tienda/tienda.html',{'productos':productos})

def categoria(request,cat_id):

	categoriap=categoriaprod.objects.get(id=cat_id)
	productos=prd.objects.filter(categorias=categoriap)
	return  render(request,'tienda/categorias.html',{'categoriap':categoriap,'productos':productos})

