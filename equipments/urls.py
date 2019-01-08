from django.urls import path
from . import views

app_name = 'equipments'

urlpatterns = [
    # Equipments
    path('', views.EquipmentsList.as_view(), name='equipments-list'),
    path('equipments/create/', views.EquipmentsCreate.as_view(), name='equipments-create'),
    path('equipments/<pk>/update/', views.EquipmentsUpdate.as_view(), name='equipments-update'),
    path('equipments/<pk>/delete/', views.EquipmentsDelete.as_view(), name='equipments-delete'),

    # Type
    path('type/', views.TypeList.as_view(), name='type-list'),
    path('type/create/', views.TypeCreate.as_view(), name='type-create'),
    path('type/<pk>/update/', views.TypeUpdate.as_view(), name='type-update'),
    path('type/<pk>/delete/', views.TypeDelete.as_view(), name='type-delete'),

    # Model
    path('model/', views.ModelList.as_view(), name='model-list'),
    path('model/create/', views.ModelCreate.as_view(), name='model-create'),
    path('model/<pk>/update/', views.ModelUpdate.as_view(), name='model-update'),
    path('model/<pk>/delete/', views.ModelDelete.as_view(), name='model-delete'),

    # Lan
    path('lan/', views.LanList.as_view(), name='lan-list'),
    path('lan/create/', views.LanCreate.as_view(), name='lan-create'),
    path('lan/<pk>/update/', views.LanUpdate.as_view(), name='lan-update'),
    path('lan/<pk>/delete/', views.LanDelete.as_view(), name='lan-delete'),

]