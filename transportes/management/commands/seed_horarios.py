# transportes/management/commands/seed_horarios.py
from django.core.management.base import BaseCommand

from transportes.models import Empresa, Horario, Linha, Localidade

# (hora_saida, via, frequencia, sentido)
HORARIOS = [
    # --- Saída: Rodoviária (ex-"Convencional") ---
    ("05:00", "José Luis / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("06:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("06:35", "Tanac / São Paulo", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("07:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("07:35", "Tanac / São Paulo", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("08:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("08:35", "José Luis / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("09:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("09:35", "José Luis / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("10:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("10:35", "José Luis / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("11:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("11:35", "José Luis / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("12:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("12:35", "José Luis / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("13:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("13:35", "José Luis / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("14:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("14:35", "José Luis / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("15:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),  # * passa pelo Hospital Montenegro
    ("15:35", "José Luis / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("16:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("16:35", "Tanac / São Paulo", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("17:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("17:35", "Tanac / São Paulo", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("18:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),  # ** via Unisc em período letivo
    ("18:35", "Tanac / São Paulo", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("19:00", "Tanac / São Paulo", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("20:00", "Tanac / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("21:00", "Tanac / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("22:20", "Tanac / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),  # ** via Unisc em período letivo
    ("23:15", "José Luis / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("00:05", "José Luis / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),

    # --- Saída: Germano Henke ---
    ("05:20", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("06:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("07:00", "Zootecnia / Tanac", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("07:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("08:00", "Zootecnia / Tanac", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("08:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("09:00", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("09:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("10:00", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("10:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("11:00", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("11:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("12:00", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("12:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("13:00", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("13:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("14:00", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("14:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),  # * passa pelo Hospital Montenegro
    ("15:00", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("15:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("16:00", "São Paulo / Av. Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("16:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("17:00", "Zootecnia / Tanac", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("17:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("18:00", "Zootecnia / Tanac", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("18:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),  # ** via Unisc em período letivo
    ("19:00", "Zootecnia / Tanac", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("19:30", "Zootecnia / Tanac", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("20:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("21:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("22:50", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SEX, "Germano Henke"),
    ("23:35", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SAB, "Germano Henke"),
    ("00:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SAB, "Germano Henke"),
]


class Command(BaseCommand):
    help = "Popula o banco com os horários reais da linha Convencional (Urbano Montenegro / SILAS)"

    def handle(self, *args, **options):
        empresa, _ = Empresa.objects.get_or_create(
            nome="SILAS - Serviços de Transportes Urbanos Ltda"
        )
        rodoviaria, _ = Localidade.objects.get_or_create(
            nome="Rodoviária", defaults={"e_centro": True}
        )

        # Remove qualquer Linha antiga com esses nomes (e os Horario ligados a
        # elas, via CASCADE) para começar limpo, evitando duplicatas de tentativas anteriores.
        linhas_antigas = Linha.objects.filter(nome__in=["Convencional", "Linha Germano Henke"])
        removidas, _ = linhas_antigas.delete()
        if removidas:
            self.stdout.write(self.style.WARNING(f"{removidas} registro(s) antigo(s) removido(s)."))

        linha, _ = Linha.objects.get_or_create(
            nome="Convencional",
            empresa=empresa,
            defaults={"origem": rodoviaria, "tipo": Linha.Tipo.URBANO},
        )

        criados = 0
        for hora, via, frequencia, sentido in HORARIOS:
            Horario.objects.create(
                linha=linha,
                hora_saida=hora,
                via=via,
                frequencia=frequencia,
                sentido=sentido,
            )
            criados += 1

        self.stdout.write(self.style.SUCCESS(f"Concluído! {criados} horários criados na linha Convencional."))
