# transportes/management/commands/seed_horarios_interiorano.py
from django.core.management.base import BaseCommand

from transportes.models import Empresa, Horario, Linha, Localidade

SEG_SEX = Horario.Frequencia.SEG_SEX
SEG_SAB = Horario.Frequencia.SEG_SAB
SABADO = Horario.Frequencia.SABADO
QUARTA = Horario.Frequencia.QUARTA

# Fonte: VIMSA - Linhas Municipais Interioranas de Montenegro
# Aprovado por Eliardo Rael Gehm

# ============================================================
# LINHA: Santos Reis
# ============================================================
SANTOS_REIS = [
    # (hora_saida, via, frequencia, sentido, observacoes)
    ("12:30", "Alfama", SEG_SEX, "Rodoviária", ""),
    ("06:40", "Alfama", SEG_SEX, "Santos Reis", ""),
]

# ============================================================
# LINHA: Bom Jardim
# ============================================================
BOM_JARDIM = [
    ("07:20", "Costa da Serra", SEG_SEX, "Rodoviária", ""),
    ("10:55", "Costa da Serra", SEG_SEX, "Rodoviária", ""),
    ("12:15", "Costa da Serra", SABADO, "Rodoviária", ""),
    ("16:20", "Costa da Serra", SEG_SEX, "Rodoviária", ""),

    ("07:15", "Costa da Serra", SABADO, "Bom Jardim", ""),
    ("08:05", "Costa da Serra", SEG_SEX, "Bom Jardim", ""),
    ("11:40", "Costa da Serra", SEG_SEX, "Bom Jardim", ""),
    ("17:05", "Costa da Serra", SEG_SEX, "Bom Jardim", ""),
]

# ============================================================
# LINHA: Porto Garibaldi
# ============================================================
PORTO_GARIBALDI = [
    ("12:30", "Vendinha", SEG_SAB, "Rodoviária", ""),

    ("06:10", "Vendinha", SEG_SEX, "Porto Garibaldi", ""),
    ("07:15", "Vendinha", SABADO, "Porto Garibaldi", ""),
    ("13:20", "RS124", SEG_SAB, "Porto Garibaldi", ""),
]

# ============================================================
# LINHA: Serra Velha
# ============================================================
SERRA_VELHA = [
    ("12:15", "Catupi", QUARTA, "Rodoviária", ""),
    ("17:35", "Catupi", SEG_SEX, "Rodoviária", ""),

    ("05:50", "Catupi", SEG_SEX, "Serra Velha", ""),
    ("13:30", "Catupi", QUARTA, "Serra Velha", ""),
]

LINHAS_INTERIORANAS = {
    "Santos Reis": {"destino": "Santos Reis", "horarios": SANTOS_REIS},
    "Bom Jardim": {"destino": "Bom Jardim", "horarios": BOM_JARDIM},
    "Porto Garibaldi": {"destino": "Porto Garibaldi", "horarios": PORTO_GARIBALDI},
    "Serra Velha": {"destino": "Serra Velha", "horarios": SERRA_VELHA},
}


class Command(BaseCommand):
    help = "Popula o banco com os horários reais das linhas interioranas municipais de Montenegro (VIMSA)"

    def handle(self, *args, **options):
        empresa, _ = Empresa.objects.get_or_create(
            nome="VIMSA - Viação Montenegro S.A."
        )
        rodoviaria = Localidade.objects.get(nome="Rodoviária")

        nomes_para_remover = list(LINHAS_INTERIORANAS.keys())
        removidas, _ = Linha.objects.filter(nome__in=nomes_para_remover).delete()
        if removidas:
            self.stdout.write(self.style.WARNING(f"{removidas} registro(s) antigo(s) removido(s)."))

        total_criados = 0
        for nome_linha, config in LINHAS_INTERIORANAS.items():
            destino, _ = Localidade.objects.get_or_create(nome=config["destino"])

            linha, _ = Linha.objects.get_or_create(
                nome=nome_linha,
                empresa=empresa,
                defaults={
                    "origem": rodoviaria,
                    "destino": destino,
                    "tipo": Linha.Tipo.INTERIORANO,
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
            f"Concluído! {total_criados} horários criados em {len(LINHAS_INTERIORANAS)} linhas interioranas."
        ))
