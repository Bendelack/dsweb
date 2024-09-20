from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'nome de usuário...'}),
            'password': forms.PasswordInput(attrs={'placeholder':'senha...'}),
        }

class Balancete(models.Model):
    nome = models.CharField(max_length=20)
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class BalanceteForm(ModelForm):
    class Meta:
        model = Balancete
        fields = ['nome', 'data']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'nome do balancete...'}),
            'data': forms.DateInput(attrs={'type':'date'}),
        }

class Receita(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField('Descrição')
    data = models.DateField()
    valor = models.FloatField()
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)

    def __str__(self):
        return  self.nome

class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'descricao', 'data', 'valor', 'balancete']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'receita...'}),
            'descricao': forms.Textarea(attrs={'placeholder':'descrição da receita...'}),
            'data': forms.DateInput(attrs={'type':'date'}),
            'valor': forms.NumberInput(attrs={'placeholder':'valor...'}),
        }

class Despesa(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField('Descrição')
    data = models.DateField()
    valor = models.FloatField()
    foto_boleto = models.ImageField(upload_to='boletos')
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)

    def __str__(self):
        return  self.nome

class DespesaForm(ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'descricao', 'data', 'valor', 'foto_boleto', 'balancete']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'despesa...'}),
            'descricao': forms.Textarea(attrs={'placeholder':'descrição da despesa...'}),
            'data': forms.DateInput(attrs={'type':'date'}),
            'valor': forms.NumberInput(attrs={'placeholder':'valor...'}),
            'foto_boleto': forms.ClearableFileInput(),
        }