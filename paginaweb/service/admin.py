from django.contrib import admin
from service.models import service
# Register your models here.
class serviceAdmin(admin.ModelAdmin):
	list_display=('titulo','contenido','imagenes','created','update')
	search_fields=('nombre','telefono')
	list_filter=('update',)
	date_hierarchy='update'
	readonly_fields=('created','update')

admin.site.register(service,serviceAdmin)
