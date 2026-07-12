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


class Rota(models.Model):
    """Liga uma origem a um destino, operada por uma empresa."""

    origem = models.ForeignKey(Localidade, on_delete=models.CASCADE, related_name="rotas_origem") # Ex.: montenegro.rotas_origem.all()
    destino = models.ForeignKey(Localidade, on_delete=models.CASCADE, related_name="rotas_destino")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="rotas")

    class Meta:
        """Configurações e regras do modelo."""

        verbose_name = "Rota"
        verbose_name_plural = "Rotas"

        # Impede rotas duplicadas para a mesma empresa.
        constraints = [
            models.UniqueConstraint(
                fields=["origem", "destino", "empresa"],
                name="rota_unica_por_empresa"
            )
        ]

    def __str__(self):
            """Representação legível da rota."""
            return f"{self.origem} -> {self.destino} ({self.empresa})"

    def clean(self):
        """Valida as regras de negócio da rota."""

        # Origem e destino não podem ser a mesma localidade.
        if self.origem_id and self.origem_id == self.destino_id:
            raise ValidationError("A origem não pode ser igual ao destino.")

    def save(self, *args, **kwargs):
        """Valida o modelo antes de salvá-lo."""
        self.full_clean()
        super().save(*args, **kwargs)


class Horario(models.Model):
    """Um horário específico dentro de uma rota."""

    class DiaSemana(models.IntegerChoices):
        """Dias da semana permitidos para um horário."""

        SEGUNDA = 0, "Segunda-feira"
        TERCA = 1, "Terça-feira"
        QUARTA = 2, "Quarta-feira"
        QUINTA = 3, "Quinta-feira"
        SEXTA = 4, "Sexta-feira"
        SABADO = 5, "Sábado"
        DOMINGO = 6, "Domingo"

    rota = models.ForeignKey(Rota, on_delete=models.CASCADE, related_name="horarios") # Ex.: rota.horarios.all()
    dia_semana = models.IntegerField(choices=DiaSemana.choices)
    hora_saida = models.TimeField()
    preco_estimado = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "Horário"
        verbose_name_plural = "Horários"
        ordering = ["dia_semana", "hora_saida"]

    def __str__(self):
        return f"{self.rota} - {self.get_dia_semana_display()} {self.hora_saida}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super.save(*args, **kwargs)

