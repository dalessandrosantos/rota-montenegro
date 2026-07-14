from django.shortcuts import render
from .models import Linha

def home(request):
    return render(request, "transportes/home.html")


def urbano(request):
    linhas = Linha.objects.filter(tipo=Linha.Tipo.URBANO)

    # Ordena os horários de cada linha, mantendo horários da madrugada no final
    for linha in linhas:
        horarios_ordenados = sorted(
            linha.horarios.all(),
            key=lambda h: (h.hora_saida.hour < 4, h.hora_saida)
        )

        grupos = {}
        for horario in horarios_ordenados:
            grupos.setdefault(horario.sentido, []).append(horario)

        linha.grupos_sentido = grupos

    context = {"linhas": linhas}
    return render(request, "transportes/horarios_urbano.html", context)

