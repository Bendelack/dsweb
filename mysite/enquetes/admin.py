from django.contrib import admin

from .models import Pergunta, Alternativa, Rotulo, Autor

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['texto', 'rotulos']}),
        ('informações de data:', {'fields': ['data_pub', 'data_fim']}),
        ('autor:', {'fields': ['autor']}),
    ]
    inlines = [AlternativaInline]
    list_display = ('texto', 'id', 'data_pub', 'publicada_recentemente')
    list_filter = ['data_pub']
    search_fields = ['texto']

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Rotulo)
admin.site.register(Autor)