from django.contrib import admin
from .models import categoria, post
# Register your models here.

class categoricaAdmin(admin.ModelAdmin):
	list_display=('nombre','created','update')
	
	list_filter=('update',)
	date_hierarchy='update'
	readonly_fields=('created','update')

class postAdmin(admin.ModelAdmin):
	list_display=('titulo','contenido','imagenes','created','update')
	
	list_filter=('update',)
	date_hierarchy='update'
	readonly_fields=('created','update')

admin.site.register(post,postAdmin)
admin.site.register(categoria,categoricaAdmin)

