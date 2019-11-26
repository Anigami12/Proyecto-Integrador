from django.contrib import admin

from .models import pais, ciudad, usuario, tipo_proveedor, proveedor, categoria_producto, producto, compra

admin.site.register(pais)
admin.site.register(ciudad)
admin.site.register(usuario)
admin.site.register(tipo_proveedor)
admin.site.register(proveedor)
admin.site.register(categoria_producto)
admin.site.register(producto)
admin.site.register(compra)