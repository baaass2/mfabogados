from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

from propiedades.models import propiedad, categoria

def catalogo(request):
    get_arriendo = request.GET['arriendo']
    propiedades = propiedad.objects.filter(arriendo=get_arriendo)
    categorias = categoria.objects.all()
    
    return render(request, "catalogo.html",{"propiedades":propiedades, "categorias":categorias})


def detallePropiedad(request):
    get_propiedad = request.GET['id'] or '1'
    select_propieadad = propiedad.objects.filter(id=get_propiedad)
    return render(request, "propiedad.html", {"propiedades":select_propieadad})