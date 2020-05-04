from django.urls import path

from . import views


urlpatterns = (
    path('', views.ListVirtualCircuitsView.as_view(), name='list_virtual_circuits'),
)
