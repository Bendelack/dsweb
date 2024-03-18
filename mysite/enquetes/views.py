from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('DsWeb 2024.1 <br> Rick Hill - 20231014040026')


def detalhes(request, pergunta_id):
    resultado = 'DETALHES da enquete de número %s'
    return HttpResponse(resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = 'VOTACAO da enquete de número %s'
    return HttpResponse(resultado % pergunta_id)

def resultado(request, pergunta_id):
    resultado = 'RESULTADO da enquete de número %s'
    return HttpResponse(resultado % pergunta_id)