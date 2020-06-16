from django.urls import path
from . import views


urlpatterns = (
    path('', views.VirtualCircuitListView.as_view(), name='virtual_circuit_list'),
    path("add/", views.VirtualCircuitCreateView.as_view(), name='virtual_circuit_add'),
    path("delete/", views.VirtualCircuitBulkDeleteView.as_view(), name='virtual_circuit_bulk_delete'),
    path("add/vlan/", views.VirtualCircuitVLANCreateView.as_view(), name='virtual_circuit_vlan_add'),
    path('<int:vcid>/', views.VirtualCircuitView.as_view(), name='virtual_circuit'),
)
