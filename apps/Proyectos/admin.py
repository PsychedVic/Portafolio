from django.contrib import admin
from .models import Categoria, Proyecto, Integrante, Imagenes, AsignarImagenes, AsignarIntegrante
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Integrante)
admin.site.register(Imagenes)

class AsignarIntegranteInline(admin.TabularInline):
    '''Tabular Inline View for Detalle'''

    model = AsignarIntegrante
    extra = 1

class AsignarImagenesInline(admin.TabularInline):
    '''Tabular Inline View for Detalle'''

    model = AsignarImagenes
    extra = 1

@admin.register(Proyecto)
class FProyectoAdmin(admin.ModelAdmin):
    '''Admin View for Factura'''

    list_display = ('nombre','descripcion','fecha','categoria')

    inlines = [
        AsignarIntegranteInline,AsignarImagenesInline
    ]
   