# transportes/management/commands/seed_horarios_intermunicipal.py
from django.core.management.base import BaseCommand

from transportes.models import Empresa, Horario, Linha, Localidade

SEG_SEX = Horario.Frequencia.SEG_SEX
SABADO = Horario.Frequencia.SABADO
DOM_FERIADOS = Horario.Frequencia.DOM_FERIADOS

LEGENDA_PROMO = "* PREÇO PROMOCIONAL DE COMUM.\n"

EMBARQUES_BR448 = (
    "Embarques: Garagem Vimsa, Asun, Imec, Santos Dumont 1198, Asilo, "
    "Rodoviária de Montenegro, Escola Cinco de Maio, Hospital Unimed, "
    "Assistência, Posto Spolier, Germano Henke (entrada do bairro)."
)
DESEMBARQUES_BR448 = (
    "Desembarques: Germano Henke (entrada do bairro), Aeroclube (rótula), "
    "Posto Spolier, Assistência, Hospital Unimed, Escola Cinco de Maio, "
    "Rodoviária, Asilo, Osvaldo Aranha 1654 e Garagem Vimsa."
)

# Fonte: VIMSA - Quadro de Horários Linhas Intermunicipais
# Form Nº 182.i Rev: 29 — vigente a partir de 25/05/2026
# Aprovado por Eliardo Rael Gehm

# ============================================================
# LINHA: Montenegro – Porto Alegre via BR-386 Comum
# ============================================================
BR_386 = [
    # (hora_saida, via, frequencia, sentido, observacoes)
    ("05:10", "Via BR-386", SEG_SEX, "Montenegro", ""),
    ("11:10", "Via BR-386", SEG_SEX, "Montenegro", ""),
    ("17:10", "Via BR-386", SEG_SEX, "Montenegro", ""),
    ("06:10", "Via BR-386", SABADO, "Montenegro", ""),
    ("07:10", "Via BR-386", SABADO, "Montenegro", ""),
    ("13:10", "Via BR-386", SABADO, "Montenegro", ""),
    ("17:10", "Via BR-386", SABADO, "Montenegro", ""),
    ("07:10", "Via BR-386", DOM_FERIADOS, "Montenegro", ""),
    ("13:10", "Via BR-386", DOM_FERIADOS, "Montenegro", ""),
    ("17:10", "Via BR-386", DOM_FERIADOS, "Montenegro", ""),

    ("07:00", "Via BR-386", SEG_SEX, "Porto Alegre", ""),
    ("15:00", "Via BR-386", SEG_SEX, "Porto Alegre", ""),
    ("19:00", "Via BR-386", SEG_SEX, "Porto Alegre", ""),
    ("08:00", "Via BR-386", SABADO, "Porto Alegre", ""),
    ("09:00", "Via BR-386", SABADO, "Porto Alegre", ""),
    ("15:00", "Via BR-386", SABADO, "Porto Alegre", ""),
    ("19:00", "Via BR-386", SABADO, "Porto Alegre", ""),
    ("09:00", "Via BR-386", DOM_FERIADOS, "Porto Alegre", ""),
    ("15:00", "Via BR-386", DOM_FERIADOS, "Porto Alegre", ""),
    ("19:00", "Via BR-386", DOM_FERIADOS, "Porto Alegre", ""),
]

# ============================================================
# LINHA: Montenegro – Porto Alegre Semi Direto via BR-448
# Todos os horários com ponto de início/término na garagem da empresa.
# ============================================================
BR_448 = [
    ("06:20", "Via BR-448 *", SEG_SEX, "Montenegro", LEGENDA_PROMO + EMBARQUES_BR448),
    ("07:20", "Via BR-448 *", SEG_SEX, "Montenegro", LEGENDA_PROMO + EMBARQUES_BR448),
    ("09:20", "Via BR-448 *", SEG_SEX, "Montenegro", LEGENDA_PROMO + EMBARQUES_BR448),
    ("12:20", "Via BR-448 *", SEG_SEX, "Montenegro", LEGENDA_PROMO + EMBARQUES_BR448),
    ("14:20", "Via BR-448 *", SEG_SEX, "Montenegro", LEGENDA_PROMO + EMBARQUES_BR448),
    ("16:20", "Via BR-448 *", SEG_SEX, "Montenegro", LEGENDA_PROMO + EMBARQUES_BR448),
    ("09:20", "Via BR-448", SABADO, "Montenegro", EMBARQUES_BR448),
    ("16:20", "Via BR-448", SABADO, "Montenegro", EMBARQUES_BR448),
    ("09:20", "Via BR-448", DOM_FERIADOS, "Montenegro", EMBARQUES_BR448),
    ("16:20", "Via BR-448", DOM_FERIADOS, "Montenegro", EMBARQUES_BR448),

    ("08:00", "Via BR-448 *", SEG_SEX, "Porto Alegre", LEGENDA_PROMO + DESEMBARQUES_BR448),
    ("09:00", "Via BR-448 *", SEG_SEX, "Porto Alegre", LEGENDA_PROMO + DESEMBARQUES_BR448),
    ("11:00", "Via BR-448 *", SEG_SEX, "Porto Alegre", LEGENDA_PROMO + DESEMBARQUES_BR448),
    ("14:00", "Via BR-448 *", SEG_SEX, "Porto Alegre", LEGENDA_PROMO + DESEMBARQUES_BR448),
    ("17:00", "Via BR-448 *", SEG_SEX, "Porto Alegre", LEGENDA_PROMO + DESEMBARQUES_BR448),
    ("18:00", "Via BR-448 *", SEG_SEX, "Porto Alegre", LEGENDA_PROMO + DESEMBARQUES_BR448),
    ("11:00", "Via BR-448", SABADO, "Porto Alegre", DESEMBARQUES_BR448),
    ("18:00", "Via BR-448", SABADO, "Porto Alegre", DESEMBARQUES_BR448),
    ("11:00", "Via BR-448", DOM_FERIADOS, "Porto Alegre", DESEMBARQUES_BR448),
    ("18:00", "Via BR-448", DOM_FERIADOS, "Porto Alegre", DESEMBARQUES_BR448),
]

# ============================================================
# LINHA: Montenegro – São Leopoldo (Estação do Trensurb)
# ============================================================
SAO_LEOPOLDO = [
    ("05:10", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("05:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("06:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("07:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("09:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("11:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("13:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("15:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("16:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("17:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("18:40", "Via RS-240", SEG_SEX, "Montenegro", ""),
    ("07:40", "Via RS-240", SABADO, "Montenegro", ""),
    ("10:40", "Via RS-240", SABADO, "Montenegro", ""),
    ("14:40", "Via RS-240", SABADO, "Montenegro", ""),
    ("18:40", "Via RS-240", SABADO, "Montenegro", ""),
    ("07:40", "Via RS-240", DOM_FERIADOS, "Montenegro", ""),
    ("15:40", "Via RS-240", DOM_FERIADOS, "Montenegro", ""),
    ("18:40", "Via RS-240", DOM_FERIADOS, "Montenegro", ""),

    ("06:10", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("07:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("09:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("11:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("12:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("13:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("15:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("17:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("18:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("19:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("20:05", "Via RS-240", SEG_SEX, "São Leopoldo", ""),
    ("09:05", "Via RS-240", SABADO, "São Leopoldo", ""),
    ("12:05", "Via RS-240", SABADO, "São Leopoldo", ""),
    ("16:05", "Via RS-240", SABADO, "São Leopoldo", ""),
    ("20:05", "Via RS-240", SABADO, "São Leopoldo", ""),
    ("09:05", "Via RS-240", DOM_FERIADOS, "São Leopoldo", ""),
    ("17:05", "Via RS-240", DOM_FERIADOS, "São Leopoldo", ""),
    ("20:05", "Via RS-240", DOM_FERIADOS, "São Leopoldo", ""),
]

# ============================================================
# LINHA: Montenegro – Passo da Amora - Vendinha - Circular
# ============================================================
SIMULTANEO = "O embarque e desembarque são simultâneos."

PASSO_DA_AMORA = [
    ("07:00", "Via Ernesto Pop e RS 287", SEG_SEX, "Montenegro", SIMULTANEO),
    ("12:00", "Via Ernesto Pop e RS 287", SEG_SEX, "Montenegro", SIMULTANEO),
    ("18:00", "Via Ernesto Pop e RS 287", SEG_SEX, "Montenegro", SIMULTANEO),
]

# ============================================================
# LINHA: Maratá – Montenegro via Brochier e Costa Serra
# ============================================================
MARATA = [
    ("06:10", "Via Brochier e Costa Serra", SEG_SEX, "Maratá", ""),
    ("13:10", "Via Brochier e Costa Serra", SEG_SEX, "Maratá", ""),

    ("12:00", "Via Brochier e Costa Serra", SEG_SEX, "Montenegro", ""),
    ("18:30", "Via Brochier e Costa Serra", SEG_SEX, "Montenegro", ""),
]

LINHAS_INTERMUNICIPAIS = {
    "Montenegro – Porto Alegre via BR-386 Comum": {
        "origem": "Montenegro", "destino": "Porto Alegre", "horarios": BR_386,
    },
    "Montenegro – Porto Alegre Semi Direto via BR-448": {
        "origem": "Montenegro", "destino": "Porto Alegre", "horarios": BR_448,
    },
    "Montenegro – São Leopoldo (Estação Trensurb)": {
        "origem": "Montenegro", "destino": "São Leopoldo", "horarios": SAO_LEOPOLDO,
    },
    "Montenegro – Passo da Amora - Vendinha - Circular": {
        "origem": "Montenegro", "destino": None, "horarios": PASSO_DA_AMORA,
    },
    "Maratá – Montenegro via Brochier e Costa Serra": {
        "origem": "Maratá", "destino": "Montenegro", "horarios": MARATA,
    },
}


class Command(BaseCommand):
    help = "Popula o banco com os horários reais das linhas intermunicipais (VIMSA, vigência 25/05/2026)"

    def handle(self, *args, **options):
        empresa, _ = Empresa.objects.get_or_create(
            nome="VIMSA - Viação Montenegro S.A."
        )

        localidades = {}

        def get_localidade(nome, e_centro=False):
            if nome not in localidades:
                loc, _ = Localidade.objects.get_or_create(
                    nome=nome, defaults={"e_centro": e_centro}
                )
                localidades[nome] = loc
            return localidades[nome]

        rodoviaria = get_localidade("Rodoviária", e_centro=True)

        nomes_para_remover = list(LINHAS_INTERMUNICIPAIS.keys())
        removidas, _ = Linha.objects.filter(nome__in=nomes_para_remover).delete()
        if removidas:
            self.stdout.write(self.style.WARNING(f"{removidas} registro(s) antigo(s) removido(s)."))

        total_criados = 0
        for nome_linha, config in LINHAS_INTERMUNICIPAIS.items():
            origem = rodoviaria if config["origem"] == "Montenegro" else get_localidade(config["origem"])
            destino = None
            if config["destino"]:
                destino = rodoviaria if config["destino"] == "Montenegro" else get_localidade(config["destino"])

            linha, _ = Linha.objects.get_or_create(
                nome=nome_linha,
                empresa=empresa,
                defaults={
                    "origem": origem,
                    "destino": destino,
                    "tipo": Linha.Tipo.INTERMUNICIPAL,
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

        # Limpa a localidade "Montenegro" que ficou órfã (era usada antes, substituída por Rodoviária)
        orfas = Localidade.objects.filter(nome="Montenegro").exclude(
            id__in=Linha.objects.values_list("origem_id", flat=True)
        ).exclude(
        id__in=Linha.objects.values_list("destino_id", flat=True)
        )
        removidas_localidade, _ = orfas.delete()
        if removidas_localidade:
            self.stdout.write(self.style.WARNING("Localidade 'Montenegro' órfã removida (substituída por Rodoviária)."))


        self.stdout.write(self.style.SUCCESS(
            f"Concluído! {total_criados} horários criados em {len(LINHAS_INTERMUNICIPAIS)} linhas intermunicipais."
        ))
