from django.shortcuts import render
from .models import Linha, Horario

def home(request):
    return render(request, "transportes/home.html")


def urbano(request):
    linhas = Linha.objects.filter(tipo=Linha.Tipo.URBANO).order_by("id")

    # Ordena os horários de cada linha, mantendo horários da madrugada no final
    for linha in linhas:
        horarios_ordenados = sorted(
            linha.horarios.all(),
            key=lambda h: (h.hora_saida.hour < 4, h.hora_saida)
        )

        grupos_semana = {}
        grupos_domingo = {}
        for horario in horarios_ordenados:
            destino = (
                grupos_domingo
                if horario.frequencia == Horario.Frequencia.DOM_FERIADOS
                else grupos_semana
            )
            destino.setdefault(horario.sentido, []).append(horario)

        linha.grupos_semana = grupos_semana
        linha.grupos_domingo = grupos_domingo

    context = {"linhas": linhas}
    return render(request, "transportes/horarios_urbano.html", context)

