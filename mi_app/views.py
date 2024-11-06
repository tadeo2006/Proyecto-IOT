from django.shortcuts import render


from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'mi_app/pagina_inicio.html')


import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from .models import Venta

def grafico_ventas(request):
    # Extraer datos de la base de datos
    ventas = Venta.objects.all()
    fechas = [venta.fecha for venta in ventas]
    montos = [venta.monto for venta in ventas]

    # Crear el gráfico
    plt.figure(figsize=(6, 4))
    plt.plot(fechas, montos, marker='o')
    plt.title('Ventas por Fecha')
    plt.xlabel('Fecha')
    plt.ylabel('Monto')

    # Guardar el gráfico en un archivo temporal
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Enviar el gráfico como una imagen
    return HttpResponse(buffer.getvalue(), content_type='image/png')
