from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.

def dataEvento(request, titulo_evento):
    consulta = Evento.objects.get(titulo = titulo_evento).data_evento
    teste = f'O evento com o titulo {titulo_evento}, será no dia {consulta.date()} as {consulta.hour} horas'
    return HttpResponse(teste)

def lista_eventos(request):

    evento = Evento.objects.all()
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)

