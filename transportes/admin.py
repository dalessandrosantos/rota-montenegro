from django.contrib import admin
from .models import Localidade, Empresa, Linha, Horario

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

@admin.register(Linha)
class LinhaAdmin(admin.ModelAdmin):
    list_display = ("nome", "empresa", "origem","destino")
    list_filter = ("empresa", "origem", "destino")
    inlines = [HorarioInline]

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ("linha", "hora_saida", "via", "frequencia","preco_estimado")
    list_filter = ("frequencia",)
    search_fields = ("via",)
