# transportes/management/commands/seed_horarios.py
from django.core.management.base import BaseCommand

from transportes.models import Empresa, Horario, Linha, Localidade

# (hora_saida, via, frequencia, sentido)

# ============================================================
# LINHA: Germano Henke
# ============================================================
GERMANO_HENKE = [
    # --- Saída: Rodoviária (segunda a sábado / segunda a sexta) ---
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

    # --- Saída: Germano Henke (segunda a sábado / segunda a sexta) ---
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

    # --- Domingos e feriados: Saída Rodoviária ---
    ("05:00", "José Luis / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("06:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("07:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("08:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("09:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("10:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("11:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("12:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("13:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("14:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("15:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("16:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("17:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("18:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("19:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("20:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("21:00", "Tanac / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("23:15", "José Luis / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),
    ("00:05", "José Luis / Zootecnia", Horario.Frequencia.DOM_FERIADOS, "Rodoviária"),

    # --- Domingos e feriados: Saída Germano Henke ---
    ("05:20", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("06:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("07:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("08:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("09:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("10:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("11:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("12:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("13:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("14:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("15:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("16:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("17:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("18:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("19:30", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("20:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("21:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("23:35", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
    ("00:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.DOM_FERIADOS, "Germano Henke"),
]

# ============================================================
# LINHA: Cinco de Maio
# CORREÇÃO: o lado "Rodoviária" tinha sido cadastrado antes com
# os horários errados (duplicados do lado Maurício Cardoso). Os
# horários corretos abaixo começam às 05:50, não às 06:10.
# ============================================================
CINCO_DE_MAIO = [
    # --- Saída: Rodoviária ---
    ("05:50", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("06:30", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("06:50", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("07:10", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("07:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("08:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("08:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("09:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("09:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("10:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("10:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("11:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("11:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("12:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("12:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("13:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("13:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("14:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("14:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("15:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("15:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("16:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("16:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("17:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("17:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("18:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("18:35", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("19:05", "José Luiz / Av. Julio Renner", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("20:00", "Tanac / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("21:00", "Tanac / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("22:20", "Tanac / Zootecnia", Horario.Frequencia.SEG_SEX, "Rodoviária"),
    ("23:15", "José Luis / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),
    ("00:05", "José Luis / Zootecnia", Horario.Frequencia.SEG_SAB, "Rodoviária"),

    # --- Saída: Maurício Cardoso com RS 287 ---
    ("06:10", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("06:50", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("07:10", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("07:30", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("07:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("08:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("08:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("09:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("09:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("10:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("10:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("11:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("11:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("12:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("12:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("13:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("13:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("14:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("14:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("15:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("15:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("16:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("16:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("17:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("17:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("18:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("18:55", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("19:25", "Senai / 5 de Maio / Ivan Zimmer", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("20:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("21:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("22:50", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SEX, "Maurício Cardoso com RS 287"),
    ("23:35", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
    ("00:25", "Av. Julio Renner / Senai / Rodoviária", Horario.Frequencia.SEG_SAB, "Maurício Cardoso com RS 287"),
]

# ============================================================
# LINHA (nova): Faxinal, São João e Santo Antônio
# CORREÇÃO: no PDF original, o horário 05:55 aparece como
# "BR 470/ Santo Antnio" — corrigido para "Santo Antônio"
# (erro de digitação claro no documento fonte).
# ============================================================
FAXINAL = [
    # --- Saída: Parada do "ASUN" ---
    ("05:35", "Centro / Capitão Cruz / BR 470", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("06:30", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("07:15", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("09:55", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("10:55", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("11:55", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("12:55", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("15:55", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("16:55", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("17:55", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SAB, "Parada do ASUN"),
    ("18:55", "Centro / S.João / R. Barbosa", Horario.Frequencia.SEG_SEX, "Parada do ASUN"),

    # --- Saída: Faxinal ---
    ("05:55", "BR 470 / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("06:50", "Selma Wallauer / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("07:35", "Selma Wallauer / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("10:15", "Selma Wallauer / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("11:15", "Selma Wallauer / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("12:15", "Selma Wallauer / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("13:15", "Selma Wallauer / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("16:15", "Selma Wallauer / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("17:15", "BR 470 / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("18:15", "Selma Wallauer / Santo Antônio", Horario.Frequencia.SEG_SAB, "Faxinal"),
    ("19:15", "BR 470 / Santo Antônio", Horario.Frequencia.SEG_SEX, "Faxinal"),
]

# ============================================================
# LINHA (nova): Estação, São Paulo e São Pedro
# Todos os horários são segunda a sexta (a linha não circula aos sábados).
# ============================================================
ESTACAO = [
    # --- Saída: Hospital Montenegro ---
    ("06:05", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),
    ("06:55", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),
    ("07:45", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),
    ("11:55", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),
    ("12:45", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),
    ("13:35", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),
    ("16:05", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),
    ("16:55", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),
    ("17:45", "José Luiz / Bruno Andrade / Campos Neto", Horario.Frequencia.SEG_SEX, "Hospital Montenegro"),

    # --- Saída: Bairro Estação ---
    ("06:30", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
    ("07:20", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
    ("08:10", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
    ("12:20", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
    ("13:10", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
    ("14:00", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
    ("16:30", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
    ("17:20", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
    ("18:10", "Estação / São Paulo / São Pedro", Horario.Frequencia.SEG_SEX, "Bairro Estação"),
]

# Nome da linha → lista de horários dela
LINHAS_URBANAS = {
    "Germano Henke": GERMANO_HENKE,
    "Cinco de Maio": CINCO_DE_MAIO,
    "Faxinal, São João e Santo Antônio": FAXINAL,
    "Estação, São Paulo e São Pedro": ESTACAO,
}

# Nomes usados em tentativas anteriores, que precisam ser removidos
# para não deixar registros órfãos/duplicados no banco.
NOMES_ANTIGOS_PARA_REMOVER = [
    "Convencional",
    "Linha Germano Henke",
    "Germano Henke / Cinco de Maio",
]


class Command(BaseCommand):
    help = "Popula o banco com os horários reais das linhas urbanas de Montenegro (VIMSA/SILAS)"

    def handle(self, *args, **options):
        empresa, _ = Empresa.objects.get_or_create(
            nome="SILAS - Serviços de Transportes Urbanos Ltda"
        )
        rodoviaria, _ = Localidade.objects.get_or_create(
            nome="Rodoviária", defaults={"e_centro": True}
        )

        nomes_para_remover = list(LINHAS_URBANAS.keys()) + NOMES_ANTIGOS_PARA_REMOVER
        removidas, _ = Linha.objects.filter(nome__in=nomes_para_remover).delete()
        if removidas:
            self.stdout.write(self.style.WARNING(f"{removidas} registro(s) antigo(s) removido(s)."))

        total_criados = 0
        for nome_linha, horarios in LINHAS_URBANAS.items():
            linha, _ = Linha.objects.get_or_create(
                nome=nome_linha,
                empresa=empresa,
                defaults={"origem": rodoviaria, "tipo": Linha.Tipo.URBANO},
            )
            for hora, via, frequencia, sentido in horarios:
                Horario.objects.create(
                    linha=linha,
                    hora_saida=hora,
                    via=via,
                    frequencia=frequencia,
                    sentido=sentido,
                )
                total_criados += 1

        self.stdout.write(self.style.SUCCESS(f"Concluído! {total_criados} horários criados em {len(LINHAS_URBANAS)} linhas."))
