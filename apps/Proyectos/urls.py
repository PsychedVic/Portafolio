from django.urls import path
from . import views

app_name = "proyectos"
urlpatterns = [
    path("",views.ProyectoListView.as_view(), name="lista_proyecto"),
    path("<int:pk>/",views.ProyectoDetailView.as_view(), name="detalle_proyecto"),
    # path("<int:pk>/update/", views.RopaUpdateView.as_view(), name="update"),
    path("create/", views.ProyectoCreateView.as_view(), name="crear_proyecto"),
    path("<int:pk>/delete/", views.ProyectoDeleteView.as_view(), name="delete_proyecto"),  
    # path("factura",views.FacturaListView.as_view(), name="indexf"),
    # path("factura/<int:pk>/",views.FacturaDetailView.as_view(), name="detailf"),
    # path("factura/create/", views.FacturaCreateView.as_view(), name="createf"),
    # path("factura/<int:pk>/delete", views.FacturaDeleteView.as_view(), name="deletef"),
    # path("factura/<int:pk>/update", views.FacturaUpdateView.as_view(), name="updatef"),
]