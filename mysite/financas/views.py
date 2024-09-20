from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Balancete, Despesa, Receita, UserForm, BalanceteForm, ReceitaForm, DespesaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'financas/index.html')

# Classes de View para Balancete
@method_decorator(login_required, name='dispatch')
class CadastroBalanceteView(View):
    def get(self, request, *args, **kwargs):
        form = BalanceteForm()
        contexto = {'form': form}

        return render(request, 'financas/cadastro_balancete.html', contexto)

    def post(self, request, *args, **kwargs):
        form = BalanceteForm(request.POST, request.FILES)
        if form.is_valid():
            novo_balancete = Balancete(
                nome=form.cleaned_data['nome'],
                data=form.cleaned_data['data'],
                user=User.objects.get(pk=request.user.id),
            )
            novo_balancete.save()
            return HttpResponseRedirect(reverse('financas:gerenciar-financas'))

        contexto = {'form': form}
        return render(request, 'financas/cadastro_balancete.html', contexto)

@method_decorator(login_required, name='dispatch')
class ListaBalancetesView(View):
    def get(self, request, *args, **kwargs):
        usuario_logado = User.objects.get(pk=request.user.id)
        balancetes = usuario_logado.balancete_set.all().order_by('-data')
        contexto = {'balancetes': balancetes}
        return render(request, 'financas/lista_balancetes.html', contexto)


@method_decorator(login_required, name='dispatch')
class DetalhesBalanceteView(View):
    def get(self, request, *args, **kwargs):
        id_balancete = kwargs['pk']
        balancete = Balancete.objects.get(pk=id_balancete)
        total_receitas = balancete.receita_set.aggregate(total_receitas=Sum('valor'))['total_receitas'] or 0
        total_despesas = balancete.despesa_set.aggregate(total_despesas=Sum('valor'))['total_despesas'] or 0
        total = total_receitas - total_despesas
        contexto = {
            'balancete': balancete,
            'total_receitas': total_receitas,
            'total_despesas': total_despesas,
            'total': total
        }
        return render(request, 'financas/detalhes-balancete.html', contexto)


# Classes de View para Usuário

class CadastroUsuarioView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        contexto = {'form': form}
        return render(request, 'financas/cadastro_usuario.html', contexto)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('financas:index'))
        contexto = {'form': form}
        return render(request, 'financas/cadastro_usuario.html', contexto)


# Classes de View para Receita
@method_decorator(login_required, name='dispatch')
class CadastroReceitaView(View):
    def get(self, request, *args, **kwargs):
        form = ReceitaForm()
        usuario_logado = User.objects.get(pk=request.user.id)
        balancetes = usuario_logado.balancete_set.all()
        contexto = {'form': form, 'balancetes': balancetes}

        return render(request, 'financas/cadastro_receita.html', contexto)

    def post(self, request, *args, **kwargs):
        form = ReceitaForm(request.POST)
        if form.is_valid():
            receita = Receita(
                nome=form.cleaned_data['nome'],
                descricao=form.cleaned_data['descricao'],
                data=form.cleaned_data['data'],
                valor=form.cleaned_data['valor'],
                balancete=form.cleaned_data['balancete'],
            )

            receita.save()
            return HttpResponseRedirect(reverse('financas:gerenciar-financas'))

        usuario_logado = User.objects.get(pk=request.user.id)
        balancetes = usuario_logado.balancete_set.all()
        contexto = {'form': form, 'balancetes': balancetes}
        return render(request, 'financas/cadastro_receita.html', contexto)


# Classes de View para Despesa
@method_decorator(login_required, name='dispatch')
class CadastroDespesaView(View):
    def get(self, request, *args, **kwargs):
        form = DespesaForm()
        usuario_logado = User.objects.get(pk=request.user.id)
        balancetes = usuario_logado.balancete_set.all()
        contexto = {'form': form, 'balancetes': balancetes}

        return render(request, 'financas/cadastro_despesa.html', contexto)

    def post(self, request, *args, **kwargs):
        form = DespesaForm(request.POST, request.FILES)
        if form.is_valid():
            despesa = Despesa(
                nome=form.cleaned_data['nome'],
                descricao=form.cleaned_data['descricao'],
                data=form.cleaned_data['data'],
                valor=form.cleaned_data['valor'],
                foto_boleto=form.cleaned_data['foto_boleto'],
                balancete=form.cleaned_data['balancete'],
            )

            despesa.save()
            return HttpResponseRedirect(reverse('financas:gerenciar-financas'))

        usuario_logado = User.objects.get(pk=request.user.id)
        balancetes = usuario_logado.balancete_set.all()
        contexto = {'form': form, 'balancetes': balancetes}

        return render(request, 'financas/cadastro_despesa.html', contexto)