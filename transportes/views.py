from django.shortcuts import render
from .models import Linha, Horario

def home(request):
    return render(request, "transportes/home.html")


def urbano(request):
    linhas = Linha.objects.filter(tipo=Linha.Tipo.URBANO).order_by("id")

    for linha in linhas:
        horarios_ordenados = sorted(
            linha.horarios.all(),
            key=lambda h: (h.hora_saida.hour < 4, h.hora_saida)
        )

        grupos = {}
        for horario in horarios_ordenados:
            grupos.setdefault(horario.frequencia, {}).setdefault(horario.sentido, []).append(horario)

        grupos_ordenados = {}
        for valor, label in Horario.Frequencia.choices:
            if valor in grupos:
                sentidos = grupos[valor]
                sentidos_ordenados = dict(
                    sorted(sentidos.items(), key=lambda item: item[0] != linha.origem.nome)
                )
                grupos_ordenados[label] = sentidos_ordenados

        linha.grupos = grupos_ordenados

    context = {"linhas": linhas}
    return render(request, "transportes/horarios_urbano.html", context)

def intermunicipal(request):
    linhas = Linha.objects.filter(tipo=Linha.Tipo.INTERMUNICIPAL).order_by("id")

    for linha in linhas:
        horarios = linha.horarios.order_by("hora_saida")

        grupos = {}
        for horario in horarios:
            grupos.setdefault(horario.frequencia, {}).setdefault(horario.sentido, []).append(horario)

        grupos_ordenados = {}
        for valor, label in Horario.Frequencia.choices:
            if valor in grupos:
                sentidos = grupos[valor]
                sentidos_ordenados = dict(
                    sorted(sentidos.items(), key=lambda item: item[0] != linha.origem.nome)
                )
                grupos_ordenados[label] = sentidos_ordenados

        linha.grupos = grupos_ordenados

    context = {"linhas": linhas}
    return render(request, "transportes/horarios_intermunicipal.html", context)


def interiorano(request):
    linhas = Linha.objects.filter(tipo=Linha.Tipo.INTERIORANO).order_by("id")

    for linha in linhas:
        horarios = linha.horarios.order_by("hora_saida")

        grupos = {}
        for horario in horarios:
            grupos.setdefault(horario.sentido, []).append(horario)

        # Origem (Rodoviária) sempre primeiro, independente do sentido cronológico
        grupos_ordenados = dict(
            sorted(grupos.items(), key=lambda item: item[0] != linha.origem.nome)
        )

        linha.grupos = grupos_ordenados

    context = {"linhas": linhas}
    return render(request, "transportes/horarios_interiorano.html", context)
