from django.db import models

# Create your models here.

class service(models.Model):

	titulo=models.CharField(max_length=50)
	contenido=models.CharField(max_length=50)
	imagenes=models.ImageField(upload_to='service')
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class meta :
		verbose_name='service'
		verbose_name_plural='services'

	def __str__(self):

		return self.titulo