from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Pergunta, Alternativa
from django.views import View

# Create your views here.
"""
def IndexView(generic.ListView):
    enquetes = Pergunta.objects.order_by('-data_pub')[:10]
    contexto = { 'lista_enquetes': enquetes }
    return render(request, 'enquetes/index.html', contexto)
"""
## class IndexView funcionando normalmente
class IndexView(View):
    def get(self, request, *args, **kwargs):
        enquetes = Pergunta.objects.order_by('-data_pub')[:10]
        contexto = { 'pergunta_list': enquetes }
        return render(request, 'enquetes/index.html', contexto)

    

    # template_name = 'enquetes/index.html'
    # context_object_name = 'lista_enquetes'
    # def get_queryset(self):
    #     return Pergunta.objects.order_by('-data_pub')[:10]
"""
def DetalhesView(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = { 'enquete': pergunta }
    return render(request, 'enquetes/detalhes.html', contexto)
"""
## class DetalhesView funcionando com erro
class DetalhesView(View):
    template = 'enquetes/pergunta_detail.html'
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk'] # o atributo pk vem na variável *args
        pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
        contexto = { 'pergunta': pergunta }
        return render(request, self.template, contexto)

    def post(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk'] # o atributo pk vem na variável *args
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        try:
            alt = pergunta.alternativa_set.get(pk=request.POST['escolha'])
        except (KeyError, Alternativa.DoesNotExist):
            return render(request, self.template, {
                'pergunta': pergunta, 'error': 'Você precisa selecionar uma alternativa.',
            })
        else:
            alt.quant_votos += 1
            alt.save()
            return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta.id,)))    
    # model = Pergunta
    # template_name = 'enquetes/pergunta_detail.html'
"""
class ResultadoView(generic.DetailView):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    return render(request, 'enquetes/resultado.html', { 'enquete': pergunta })
"""
class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk'] # o atributo pk vem na variável *args
        pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
        contexto = { 'pergunta': pergunta }
        return render(request, 'enquetes/resultado.html', contexto)
    



    # model = Pergunta
    # template_name = 'enquetes/resultado.html'

"""
VIEW VOTAÇÃO VERSÃO 1
def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        alt = pergunta.alternativa_set.get(pk=request.POST['escolha'])
    except (KeyError, Alternativa.DoesNotExist):
        return render(request, 'enquetes/pergunta_detail.html', {
            'pergunta': pergunta, 'error': 'Você precisa selecionar uma alternativa.',
        })
    else:
        alt.quant_votos += 1
        alt.save()
        return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta.id,)))
"""