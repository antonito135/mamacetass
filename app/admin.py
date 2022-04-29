from django.contrib import admin
from.models import *

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo']
    search_fields = ['codigo']
    list_per_page = 3

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(HistorialCompra)
admin.site.register(Suscripcion)