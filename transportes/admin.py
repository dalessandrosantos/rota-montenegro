from django.contrib import admin
from .models import Localidade, Empresa, Rota, Horario

@admin.register(Localidade)
class LocalidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "e_centro")
    list_filter = ("e_centro",)
    search_fields = ("nome",)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone")
    search_fields = ("nome",)

class HorarioInline(admin.TabularInline):
    """Permite cadastrar horários direto na tela da Rota, sem trocar de página."""
    model = Horario
    extra = 1  # quantas linhas em branco aparecem por padrão

@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ("orige", "destino", "empresa")
    list_filter = ("origem", "destino", "empresa")
    inlines = [HorarioInline]

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ("rota", "dia_semana", "hora_saida", "preco_estimado")
    list_filter = ("dia_semana")

