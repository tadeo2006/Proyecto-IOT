from django.urls import path
from . import views

urlpatterns = [
    path('grafico_ventas/', views.grafico_ventas, name='grafico_ventas'),  # Ruta de gráfico de ventas
]
