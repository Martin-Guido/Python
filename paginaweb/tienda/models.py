from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class categoriaprod(models.Model):
	nombre=models.CharField(max_length=50)
	
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class meta :
		verbose_name='categoriaprod'
		verbose_name_plural='categoriasprod'

	def __str__(self):
		return self.nombre

class producto(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50)
	imagenes=models.ImageField(upload_to='blog',null=True,blank=True)
	categorias=models.ForeignKey(categoriaprod,on_delete=models.CASCADE)
	precio=models.FloatField()
	cantidad=models.IntegerField()
	disponibilidad=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class meta :
		verbose_name='producto'
		verbose_name_plural='productos'

	def __str__(self):
		return self.producto
