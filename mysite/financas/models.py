from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    data_criacao = models.DateTimeField('Data de Criação')
    foto_perfil = models.ImageField('Foto de Perfil', upload_to='profile', null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)

class Balancete(models.Model):
    nome = models.CharField(max_length=20)
    data = models.DateField()
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField('Descrição')
    data = models.DateField()
    valor = models.FloatField()
    balancete = models.ForeignKey(Balancete, related_name='receitas', on_delete=models.CASCADE)

    def __str__(self):
        return  self.nome

class Despesa(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField('Descrição')
    data = models.DateField()
    valor = models.FloatField()
    foto_boleto = models.ImageField(upload_to='boletos')
    balancete = models.ForeignKey(Balancete, related_name='despesas', on_delete=models.CASCADE)

    def __str__(self):
        return  self.nome