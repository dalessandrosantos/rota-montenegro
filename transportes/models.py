from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class Localidade(models.Model):
    """Representa um distrito/bairro do interior ou o Centro."""
    nome = models.CharField(max_length=100, unique=True)
    e_centro = models.BooleanField(
        default=False,
        verbose_name="É o centro da cidade?",
        help_text="Marque como True para o 'Centro' — ajuda a filtrar rotas de/para o centro.")

    class Meta:
        verbose_name = "Localidade"
        verbose_name_plural = "Localidades"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    """Empresa ou van/transporte comunitário que opera a rota."""
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome


class Linha(models.Model):

    class Tipo(models.TextChoices):
        INTERMUNICIPAL = "INTERMUNICIPAL", "Intermunicipal"
        INTERIORANO = "INTERIORANO", "Interiorano"
        URBANO = "URBANO", "Urbano"
        SELETIVO = "SELETIVO", "Seletivo"

    nome = models.CharField(max_length=150)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="linhas")
    origem = models.ForeignKey(Localidade, on_delete=models.CASCADE, related_name="linhas_origem")
    destino = models.ForeignKey(Localidade, on_delete=models.CASCADE, related_name="linhas_destino", null=True, blank=True, help_text="Deixe em branco para linhas urbanas circulares (sem destino fixo).")
    tipo = models.CharField(max_length=20, choices=Tipo.choices)

    class Meta:
        verbose_name = "Linha"
        verbose_name_plural = "Linhas"
        constraints = [
            models.UniqueConstraint(
                fields=["nome", "empresa"],
                name="linha_nome_unico_por_empresa",
            )
        ]

    def __str__(self):
        return f"{self.nome} ({self.empresa})"

    def clean(self):
        if self.origem_id and self.destino_id and self.origem_id == self.destino_id:
            raise ValidationError("A origem não pode ser igual ao destino.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Horario(models.Model):
    """Um horário específico dentro de uma linha."""

    class Frequencia(models.TextChoices):

        SEG_SEX = "SEG_SEX", "Segunda a Sexta"
        SEG_SAB = "SEG_SAB", "Segunda a Sábado"
        TODOS_DIAS = "TODOS_DIAS", "Todos os dias"
        DOM_FERIADOS = "DOM_FERIADOS", "Domingos e Feriados"


    linha = models.ForeignKey(Linha, on_delete=models.CASCADE, related_name="horarios")
    sentido = models.CharField(max_length=120, help_text="Ex.: Rodoviária, Germano Henke, Hospital MOntenegro...")
    hora_saida = models.TimeField()
    via = models.CharField(max_length=225, help_text="Trajeto/pontos por onde passa, ex: 'Tanac / São Paulo'.")
    frequencia = models.CharField(max_length=20, choices=Frequencia.choices)
    preco_estimado = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,  # nem toda fonte de dados informa preço deixei opcional
        validators=[MinValueValidator(0)]
    )


    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Horários"
        ordering = ["hora_saida"]

    def __str__(self):
        return f"{self.linha} - {self.hora_saida} ({self.get_frequencia_display()})"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

