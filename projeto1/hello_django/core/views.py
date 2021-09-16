from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')

def soma(request, n1, n2):
    return HttpResponse(f'A soma dos numeros são:<br>Numero 1: {n1}<br>Numero 2: {n2}<br>{n1} + {n2} = {n1+n2}')

def subtracao(request, n1, n2):
    return HttpResponse(f'A subtração dos numeros são:<br>Numero 1: {n1}<br>Numero 2: {n2}<br>{n1} - {n2} = {n1-n2}')

def divisao(request, n1, n2):
    return HttpResponse(f'A divisão dos numeros são:<br>Numero 1: {n1}<br>Numero 2: {n2}<br>{n1} / {n2} = {n1/n2}')

def multiplicacao(request, n1, n2):
    return HttpResponse(f'A multiplicação dos numeros são:<br>Numero 1: {n1}<br>Numero 2: {n2}<br>{n1} * {n2} = {n1*n2}')