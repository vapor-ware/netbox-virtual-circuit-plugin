from django.urls import path
from . import views


urlpatterns = (
    path('', views.ListVirtualCircuitsView.as_view(), name='virtual_circuit_list'),
    path("add/", views.CreateVirtualCircuitView.as_view(), name='virtual_circuit_add'),
    path("add/vlan/", views.CreateVirtualCircuitVLANView.as_view(), name='virtual_circuit_vlan_add'),
    path('<int:vcid>/', views.VirtualCircuitView.as_view(), name='virtual_circuit'),
)
