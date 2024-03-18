import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto = models.CharField(max_length=150)
    data_pub = models.DateTimeField('Data de publicação')
    def __str__(self):
        return '{} ({})'.format(self.texto, self.id)

    def publicada_recentemente(self):
        agora = timezone.now()
        return self.data_pub >= agora - datetime.timedelta(hours=24)

class Alternativa(models.Model):
    texto = models.CharField(max_length=150)
    quant_votos = models.IntegerField('Quantidade de votos', default=0)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    def __str__(self):
        return '{} ({})'.format(self.texto, self.id)