from django.urls import path
from . import views


urlpatterns = (
    # Virtual Circuit.
    path('', views.VirtualCircuitListView.as_view(), name='virtual_circuit_list'),
    path("add/", views.VirtualCircuitCreateView.as_view(), name='virtual_circuit_add'),
    path("delete/", views.VirtualCircuitBulkDeleteView.as_view(), name='virtual_circuit_bulk_delete'),
    path('<int:pk>/', views.VirtualCircuitView.as_view(), name='virtual_circuit'),
    path('<int:pk>/edit/', views.VirtualCircuitEditView.as_view(), name='virtual_circuit_edit'),
    path('<int:pk>/delete/', views.VirtualCircuitDeleteView.as_view(), name='virtual_circuit_delete'),

    # Virtual-Circuit-to-VLAN connections.
    path("vlan/", views.VirtualCircuitVLANListView.as_view(), name='virtual_circuit_vlan_list'),
    path("vlan/add/", views.VirtualCircuitVLANCreateView.as_view(), name='virtual_circuit_vlan_add'),
    path("vlan/delete/", views.VirtualCircuitVLANBulkDeleteView.as_view(), name='virtual_circuit_vlan_bulk_delete'),
)
