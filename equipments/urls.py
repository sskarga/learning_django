from django.urls import path
from . import views

app_name = 'equipments'

urlpatterns = [
    path('', views.EquipmentsList.as_view(), name='home'),
    path('type/', views.TypeList.as_view(), name='type-list'),
    path('state/', views.StateList.as_view(), name='state-list'),
    path('model/', views.ModelList.as_view(), name='model-list'),
    path('lan/', views.LanList.as_view(), name='lan-list'),
    path('port/<int:id>/', views.PortList.as_view(), name='port-list'),
]