from django.urls import path
from . import views

app_name = 'location'

urlpatterns = [
    path('', views.List.as_view(), name='list'),
    path('<int:id>/', views.List.as_view(), name='list'),
    path('<int:id>/create/', views.Create.as_view(), name='create'),
    path('<int:id>/update/', views.Update.as_view(), name='update'),
    path('<int:id>/delete/', views.Delete.as_view(), name='delete'),
]
