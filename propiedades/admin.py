from django.contrib import admin
from .models import propiedad, imagenPropiedad, categoria
# Register your models here.

class imagenPropiedadAdmin(admin.TabularInline):
    model = imagenPropiedad

class propiedadAdmin(admin.ModelAdmin):
    inlines = [
        imagenPropiedadAdmin
    ]
    readonly_fields=('created','updated')

admin.site.register(propiedad, propiedadAdmin)
admin.site.register(categoria)
