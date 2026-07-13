from django.shortcuts import render
from .models import Linha

def home(request):
    return render(request, "transportes/home.html")

def urbano(request):
    dados = Linha.objects.filter(tipo=Linha.Tipo.URBANO)
    context = {"linhas": dados}
    return render(request, "transportes/horarios_urbano.html", context)
