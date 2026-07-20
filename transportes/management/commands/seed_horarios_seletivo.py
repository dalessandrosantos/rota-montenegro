# transportes/management/commands/seed_horarios_seletivo.py
from django.core.management.base import BaseCommand

from transportes.models import Empresa, Horario, Linha, Localidade

SEG_SEX = Horario.Frequencia.SEG_SEX
SEG_SAB = Horario.Frequencia.SEG_SAB
TODOS_DIAS = Horario.Frequencia.TODOS_DIAS
DOM_FERIADOS = Horario.Frequencia.DOM_FERIADOS

ATE_RODOVIARIA = "* Até a Rodoviária."

# Fonte: VIMSA - Linhas Urbanas Seletivas
# Aprovado por Eliardo Rael Gehm

# ============================================================
# LINHA: Seletivo Linha 1 e 2 - Germano Henke
# Circuito: Rodoviária / Germano Henke / Centro / Santo Antônio / Rodoviária
# ============================================================
SELETIVO_GERMANO_HENKE = [
    # (hora_saida, via, frequencia, sentido, observacoes)
    ("06:05", "José Luiz / Zootecnia", SEG_SEX, "Rodoviária", ""),
    ("06:35", "Tanac / São Paulo", SEG_SAB, "Rodoviária", ""),
    ("07:05", "José Luiz / Zootecnia", SEG_SEX, "Rodoviária", ""),
    ("07:35", "Tanac / São Paulo", SEG_SAB, "Rodoviária", ""),
    ("08:05", "José Luiz / Zootecnia", SEG_SEX, "Rodoviária", ""),
    ("08:35", "Tanac / São Paulo", TODOS_DIAS, "Rodoviária", ""),
    ("09:35", "Tanac / São Paulo", TODOS_DIAS, "Rodoviária", ""),
    ("10:35", "Tanac / São Paulo", SEG_SAB, "Rodoviária", ""),
    ("10:35", "Tanac / São Paulo", DOM_FERIADOS, "Rodoviária", ""),
    ("11:35", "Tanac / São Paulo", SEG_SAB, "Rodoviária", ""),
    ("12:35", "Tanac / São Paulo", SEG_SAB, "Rodoviária", ""),
    ("13:35", "Tanac / São Paulo", TODOS_DIAS, "Rodoviária", ""),
    ("14:35", "Tanac / São Paulo", TODOS_DIAS, "Rodoviária", ""),
    ("15:35", "Tanac / São Paulo", TODOS_DIAS, "Rodoviária", ""),
    ("16:05", "José Luiz / Zootecnia", SEG_SEX, "Rodoviária", ""),
    ("16:35", "Tanac / São Paulo", TODOS_DIAS, "Rodoviária", ""),
    ("17:05", "José Luiz / Zootecnia", SEG_SEX, "Rodoviária", ""),
    ("17:35", "Tanac / São Paulo", TODOS_DIAS, "Rodoviária", ""),
    ("18:05", "José Luiz / Zootecnia", SEG_SEX, "Rodoviária", ""),
    ("18:35", "Tanac / São Paulo", TODOS_DIAS, "Rodoviária", ""),
    ("19:35", "Tanac / São Paulo", SEG_SAB, "Rodoviária", ""),

    ("06:25", "São Paulo / Av. Ivan Zimmer", SEG_SEX, "Germano Henke", ""),
    ("06:55", "Zootecnia / Tanac", SEG_SAB, "Germano Henke", ""),
    ("07:25", "São Paulo / Av. Ivan Zimmer", SEG_SEX, "Germano Henke", ""),
    ("07:55", "Zootecnia / Tanac", SEG_SAB, "Germano Henke", ATE_RODOVIARIA),
    ("08:25", "São Paulo / Av. Ivan Zimmer", SEG_SEX, "Germano Henke", ""),
    ("08:55", "Zootecnia / Tanac", TODOS_DIAS, "Germano Henke", ""),
    ("09:55", "Zootecnia / Tanac", TODOS_DIAS, "Germano Henke", ATE_RODOVIARIA),
    ("10:55", "Zootecnia / Tanac", SEG_SAB, "Germano Henke", ""),
    ("10:55", "Zootecnia / Tanac", DOM_FERIADOS, "Germano Henke", ""),
    ("11:55", "Zootecnia / Tanac", SEG_SAB, "Germano Henke", ""),
    ("12:55", "Zootecnia / Tanac", SEG_SAB, "Germano Henke", ""),
    ("13:55", "Zootecnia / Tanac", TODOS_DIAS, "Germano Henke", ATE_RODOVIARIA),
    ("14:55", "Zootecnia / Tanac", TODOS_DIAS, "Germano Henke", ATE_RODOVIARIA),
    ("15:55", "Zootecnia / Tanac", TODOS_DIAS, "Germano Henke", ""),
    ("16:25", "São Paulo / Av. Ivan Zimmer", SEG_SEX, "Germano Henke", ATE_RODOVIARIA),
    ("16:55", "Zootecnia / Tanac", TODOS_DIAS, "Germano Henke", ""),
    ("17:25", "São Paulo / Av. Ivan Zimmer", SEG_SEX, "Germano Henke", ""),
    ("17:55", "Zootecnia / Tanac", TODOS_DIAS, "Germano Henke", ""),
    ("18:25", "São Paulo / Av. Ivan Zimmer", SEG_SEX, "Germano Henke", ""),
    ("18:55", "Zootecnia / Tanac", TODOS_DIAS, "Germano Henke", ATE_RODOVIARIA),
    ("19:55", "Zootecnia / Tanac / Centro", SEG_SEX, "Germano Henke", ""),

    # Continuação do circuito: Centro e Santo Antônio
    ("06:40", "Panorama", SEG_SEX, "Centro", ""),
    ("07:15", "Ext. Ramiro Barcelos", SEG_SAB, "Centro", ""),
    ("07:40", "Panorama", SEG_SEX, "Centro", ""),
    ("08:15", "Até Rodoviária", SEG_SAB, "Centro", ATE_RODOVIARIA),
    ("08:40", "Até Rodoviária", SEG_SEX, "Centro", ATE_RODOVIARIA),
    ("09:15", "Ext. Ramiro Barcelos", TODOS_DIAS, "Centro", ""),
    ("10:15", "Até Rodoviária", TODOS_DIAS, "Centro", ATE_RODOVIARIA),
    ("11:15", "Ext. Ramiro Barcelos", SEG_SAB, "Centro", ""),
    ("11:15", "Ext. Ramiro Barcelos", DOM_FERIADOS, "Centro", ""),
    ("12:15", "Ext. Ramiro Barcelos", SEG_SAB, "Centro", ""),
    ("13:15", "Ext. Ramiro Barcelos", SEG_SAB, "Centro", ""),
    ("14:15", "Até Rodoviária", TODOS_DIAS, "Centro", ATE_RODOVIARIA),
    ("15:15", "Até Rodoviária", TODOS_DIAS, "Centro", ATE_RODOVIARIA),
    ("16:15", "Ext. Ramiro Barcelos", TODOS_DIAS, "Centro", ""),
    ("16:40", "Panorama", SEG_SEX, "Centro", ATE_RODOVIARIA),
    ("17:15", "Até Rodoviária", TODOS_DIAS, "Centro", ATE_RODOVIARIA),
    ("17:40", "Panorama", SEG_SEX, "Centro", ""),
    ("18:15", "Ext. Ramiro Barcelos", TODOS_DIAS, "Centro", ""),
    ("18:40", "Panorama", SEG_SEX, "Centro", ""),
    ("19:15", "Até Rodoviária", TODOS_DIAS, "Centro", ATE_RODOVIARIA),

    ("06:50", "Rodoviária/Centro/Germano Henke", SEG_SEX, "Santo Antônio", ""),
    ("07:20", "Rodoviária/Centro/Germano Henke", SEG_SAB, "Santo Antônio", ""),
    ("07:50", "Rodoviária/Centro/Germano Henke", SEG_SEX, "Santo Antônio", ""),
    ("09:20", "Rodoviária/Centro/Germano Henke", TODOS_DIAS, "Santo Antônio", ""),
    ("11:20", "Rodoviária/Centro/Germano Henke", SEG_SAB, "Santo Antônio", ""),
    ("11:20", "Rodoviária/Centro", DOM_FERIADOS, "Santo Antônio", ""),
    ("12:20", "Rodoviária/Centro/Germano Henke", SEG_SAB, "Santo Antônio", ""),
    ("13:20", "Rodoviária/Centro/Germano Henke", SEG_SAB, "Santo Antônio", ""),
    ("16:20", "Rodoviária/Centro/Germano Henke", TODOS_DIAS, "Santo Antônio", ""),
    ("17:50", "Rodoviária/Centro/Germano Henke", SEG_SEX, "Santo Antônio", ""),
    ("18:20", "Rodoviária/Centro/Germano Henke", TODOS_DIAS, "Santo Antônio", ""),
    ("18:50", "Rodoviária/Centro", SEG_SEX, "Santo Antônio", ""),
]

SELETIVO_CINCO_DE_MAIO = [
    # (hora_saida, via, frequencia, sentido, observacoes)

    # Sentido: Centro
    ("06:00", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("06:30", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("06:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("07:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("07:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("08:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("08:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("09:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("09:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("10:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("10:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("11:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("11:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("12:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("12:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("13:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("13:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("14:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("14:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("15:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("15:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("16:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("16:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("17:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("17:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("18:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),
    ("18:55", "Progresso/Rui Barbosa", SEG_SAB, "Centro", ""),
    ("19:25", "Progresso / RS 287", SEG_SEX, "Centro", ""),

    # Sentido: São João
    ("06:05", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("06:35", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("07:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("07:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("08:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("08:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("09:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("09:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("10:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("10:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("11:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("11:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("12:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("12:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("13:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("13:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("14:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("14:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("15:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("15:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("16:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("16:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("17:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("17:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("18:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("18:33", "Rodoviária/Centro/Senai", SEG_SEX, "São João", ""),
    ("19:03", "Rodoviária/Centro/Senai", SEG_SAB, "São João", ""),
    ("19:33", "Rodoviária", SEG_SEX, "São João", ""),

    # Sentido: Rodoviária
    ("06:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("06:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("07:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("07:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("08:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("08:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("09:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("09:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("10:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("10:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("11:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("11:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("12:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("12:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("13:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("13:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("14:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("14:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("15:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("15:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("16:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("16:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("17:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("17:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("18:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),
    ("18:50", "José Luiz/Senai", SEG_SEX, "Rodoviária", ""),
    ("19:20", "José Luiz/Senai", SEG_SAB, "Rodoviária", ""),

    # Sentido: Senai
    ("06:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("07:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("07:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("08:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("08:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("09:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("09:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("10:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("10:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("11:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("11:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("12:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("12:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("13:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("13:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("14:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("14:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("15:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("15:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("16:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("16:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("17:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("17:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("18:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("18:40", "Centro/Progresso/Rui Barbosa", SEG_SAB, "Senai", ""),
    ("19:10", "Centro / Progresso / RS 287", SEG_SEX, "Senai", ""),
    ("19:40", "Centro", SEG_SAB, "Senai", ""),
]

LINHAS_SELETIVAS = {
    "Seletivo Linha 1 e 2 - Germano Henke": {
        "destino": None, "horarios": SELETIVO_GERMANO_HENKE,
    },
    "Seletivo Linha 3 e 4 - Cinco de Maio": {
        "destino": None, "horarios": SELETIVO_CINCO_DE_MAIO,
    },
}


class Command(BaseCommand):
    help = "Popula o banco com os horários reais das linhas urbanas seletivas (VIMSA)"

    def handle(self, *args, **options):
        empresa, _ = Empresa.objects.get_or_create(
            nome="SILAS - Serviços de Transportes Urbanos Ltda"
        )
        rodoviaria = Localidade.objects.get(nome="Rodoviária")

        nomes_para_remover = list(LINHAS_SELETIVAS.keys())
        removidas, _ = Linha.objects.filter(nome__in=nomes_para_remover).delete()
        if removidas:
            self.stdout.write(self.style.WARNING(f"{removidas} registro(s) antigo(s) removido(s)."))

        total_criados = 0
        for nome_linha, config in LINHAS_SELETIVAS.items():
            destino = None
            if config["destino"]:
                destino, _ = Localidade.objects.get_or_create(nome=config["destino"])

            linha, _ = Linha.objects.get_or_create(
                nome=nome_linha,
                empresa=empresa,
                defaults={
                    "origem": rodoviaria,
                    "destino": destino,
                    "tipo": Linha.Tipo.SELETIVO,
                },
            )

            for hora, via, frequencia, sentido, observacoes in config["horarios"]:
                Horario.objects.create(
                    linha=linha,
                    hora_saida=hora,
                    via=via,
                    frequencia=frequencia,
                    sentido=sentido,
                    observacoes=observacoes,
                )
                total_criados += 1

        self.stdout.write(self.style.SUCCESS(
            f"Concluído! {total_criados} horários criados em {len(LINHAS_SELETIVAS)} linha(s) seletivas."
        ))
