from django.contrib import admin
from .models import *

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo')
    search_fields = ('titulo',)

    def resumo(self, obj):
        desc = obj.descricao
        if desc:
            if len(desc) > 40:
                return '%s...' % desc[:35]
        return desc

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'avaliacao',)

    list_filter = ('avaliacao',)
    search_fields = ('nome',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_perfil', 'resumo', 'padrao_comportamento',)
    search_fields = ('nome', 'tipo_perfil', 'padrao_comportamento',)

    def resumo(self, obj):
        desc = obj.descricao
        if desc:
            if len(desc) > 40:
                return '%s...' % desc[:35]
        return desc

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pergunta', 'perfil',)
    list_filter = ('perfil', 'pergunta',)
    search_fields = ('nome',)

@admin.register(Comportamento)
class ComportamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'perfil',)
    list_filter = ('perfil',)
    search_fields = ('nome',)

@admin.register(PontoForte)
class PontoForteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'perfil',)
    list_filter = ('perfil',)
    search_fields = ('nome',)

@admin.register(PontoDaMelhoria)
class PontoDaMelhoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'perfil',)
    list_filter = ('perfil',)
    search_fields = ('nome',)

@admin.register(Motivacao)
class MotivacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'perfil',)
    list_filter = ('perfil',)
    search_fields = ('nome',)
