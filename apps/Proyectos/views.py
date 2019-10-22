from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Proyecto, AsignarIntegrante, AsignarImagenes
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
# Create your views here.


class ProyectoListView(generic.ListView):
    model = Proyecto
    template_name = "lista_proyecto.html"

def detail(request, proyecto_id):
    p = get_object_or_404(Proyecto, pk=proyecto_id)
    return render_to_response('detalle_proyecto.html', {'proyecto': p},
                          context_instance=RequestContext(request))

class ProyectoDetailView(generic.DetailView):
    model = Proyecto
    template_name = "detalle_proyecto.html"


class AsignarIntegranteInLine(InlineFormSetFactory):
    model = AsignarIntegrante
    fields = '__all__'

class AsignarImagenesInLine(InlineFormSetFactory):
    model = AsignarImagenes
    fields = '__all__'

class ProyectoCreateView(CreateWithInlinesView):
    model = Proyecto
    inlines = [AsignarIntegranteInLine, AsignarImagenesInLine]
    fields = '__all__'
    template_name = "crear_proyecto.html"


class ProyectoDeleteView(generic.DeleteView):
    model = Proyecto
    template_name = "delete_proyecto.html"

