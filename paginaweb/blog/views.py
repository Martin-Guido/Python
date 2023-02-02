from django.shortcuts import render
from blog.models import post, categoria as cat
# Create your views here.
# Create your views here.

def blog(request):

	posts=post.objects.all()
	return  render(request,'blog/blog.html',{'posts':posts})

def categoria(request,cat_id):

	categoria=cat.objects.get(id=cat_id)
	posts=post.objects.filter(categorias=categoria)
	return  render(request,'blog/categorias.html',{'categoria':categoria,'posts':posts})

