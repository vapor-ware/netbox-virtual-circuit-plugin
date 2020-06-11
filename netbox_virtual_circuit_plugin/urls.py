from django.urls import path
from . import views


urlpatterns = (
    path('', views.ListVirtualCircuitsView.as_view(), name='list_virtual_circuits'),
    path("add/", views.CreateVirtualCircuitView.as_view(), name='virtualcircuit_add'),
    path('<int:vcid>/', views.VirtualCircuitView.as_view(), name='virtual_circuit'),
)
