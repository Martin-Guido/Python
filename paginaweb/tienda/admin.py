from django.contrib import admin

# Register your models here.
from .models import categoriaprod, producto
# Register your models here.

class categoricaprodAdmin(admin.ModelAdmin):
	list_display=('nombre','created','update')
	
	list_filter=('update',)
	date_hierarchy='update'
	readonly_fields=('created','update')

class productoAdmin(admin.ModelAdmin):
	list_display=('nombre','descripcion','imagenes','created','update')
	
	list_filter=('update',)
	date_hierarchy='update'
	readonly_fields=('created','update')

admin.site.register(producto,productoAdmin)
admin.site.register(categoriaprod,categoricaprodAdmin)

