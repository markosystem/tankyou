from django.contrib import admin
from .models import Marca, Modelo, Veiculo, Lancamento


class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo_veiculo', 'data_criacao']
    search_fields = ['nome']


class ModeloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cilindrada', 'ano', 'marca', 'data_criacao']
    search_fields = ['nome']
    fieldsets = [(None, {'fields': ['nome', 'cilindrada', 'ano', 'marca']})]


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'modelo', 'usuario', 'data_criacao']
    search_fields = ['placa']
    fieldsets = [(None, {'fields': ['placa', 'modelo', 'usuario']})]


class LancamentoAdmin(admin.ModelAdmin):
    list_display = ['veiculo', 'valor_total', 'km_inicial', 'km_final']
    fieldsets = [
        (None, {'fields': ['km_inicial', 'km_final', 'valor_total', 'data_fechamento', 'valor_por_litro', 'veiculo', 'nivel_rotacao', 'tipo_combustivel']})]


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Lancamento, LancamentoAdmin)
