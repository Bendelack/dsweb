from django.contrib import admin

from .models import Pergunta, Alternativa

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['texto']}),
        ('informações de data:', {'fields': ['data_pub']}),
    ]
    inlines = [AlternativaInline]
    list_display = ('texto', 'id', 'data_pub', 'publicada_recentemente')
    list_filter = ['data_pub']
    search_fields = ['texto']

admin.site.register(Pergunta, PerguntaAdmin)
#admin.site.register(Alternativa)