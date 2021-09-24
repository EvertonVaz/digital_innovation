from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse
# Create your views here.

def dataEvento(request, titulo_evento):
    ''' Lição que foi passada pelo professor '''
    consulta = Evento.objects.get(titulo = titulo_evento).data_evento
    teste = f'O evento com o titulo {titulo_evento}, será no dia {consulta.date()} as {consulta.hour} horas'
    return HttpResponse(teste)

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuáio ou senha inválido")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual).order_by('data_evento')
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

def historico(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario , data_evento__lt=data_atual).order_by('data_evento')
    dados = {'eventos': evento}
    return render(request , 'historico.html' , dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)

    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        endereco = request.POST.get('endereco')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.endereco = endereco
                evento.save()

        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  endereco=endereco,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).order_by('data_evento').values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)