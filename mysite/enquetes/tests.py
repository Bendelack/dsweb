import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Pergunta

# função utilitária para criação de pergunta no banco de dados
def criar_pergunta(texto, quant_dias):
    """
    Criar uma pergunta com um texto e uma data de publicação
    """
    data = timezone.now() + datetime.timedelta(days=quant_dias)
    return Pergunta.objects.create(texto=texto, data_pub=data)

class DetalhesViewTest(TestCase):
    def test_com_pergunta_no_futuro(self):
        """
        DEVE exibir o erro HTTP 404 - Identificador de enquete inválido
        """
        p = criar_pergunta('Pergunta no futuro', 1)
        url = reverse('enquetes:detalhes', args=(p.id,))
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 404)

    def test_com_pergunta_no_passado(self):
        """
        DEVE exibir os detalhes da pergunta com data no passado
        """
        p = criar_pergunta('Pergunta no passado', -1)
        url = reverse('enquetes:detalhes', args=(p.id,))
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')

class IndexViewTest(TestCase):
    def test_sem_pergunta_cadastrada(self):
        """
        É esperado a exibição do aviso de não há enquetes cadastradas.
        """
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(resposta.context['pergunta_list'], [])

    def test_com_pergunta_no_futuro(self):
        """
        É esperado a exibição do aviso de não há enquetes cadastradas.
        """
        criar_pergunta('pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Nenhuma enquete cadastrada')
        self.assertQuerysetEqual(resposta.context['pergunta_list'], [])

    def test_com_pergunta_no_passado(self):
        """
        É esperado qua a pergunta apareçana lista
        """
        criar_pergunta('Pergunta no passado', -1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')
        self.assertQuerysetEqual(resposta.context['pergunta_list'], ['<Pergunta: Pergunta no passado>'])

    def test_com_pergunta_no_passado_e_outra_no_futuro(self):
        """
        DEVE ser apresentada apenas a pergunta com data no passado
        """
        criar_pergunta('Pergunta no passado', -1)
        criar_pergunta('Pergunta no futuro', 1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'Pergunta no passado')
        self.assertQuerysetEqual(resposta.context['pergunta_list'], ['<Pergunta: Pergunta no passado>'])

    def test_com_duas_perguntas_no_passado_verificando_a_ordenacao(self):
        """
        DEVE exibir as perguntas no passado ordenadas decrescentemente por data
        """
        criar_pergunta('Pergunta no passado 1', -2)
        criar_pergunta('Pergunta no passado 2', -1)
        resposta = self.client.get(reverse('enquetes:index'))
        self.assertContains(resposta, 'Pergunta no passado 1')
        self.assertContains(resposta, 'Pergunta no passado 2')
        self.assertQuerysetEqual(resposta.context['pergunta_list'], ['<Pergunta: Pergunta no passado 2>', '<Pergunta: Pergunta no passado 1>'])

# Create your tests here.
class PerguntaModelTest(TestCase):
    def test_publicada_recentemente_pergunta_no_futuro(self):
        """
        O método para pergunta no futuro DEVE retornar False
        """
        tempo = timezone.now() + datetime.timedelta(seconds=1)
        p = Pergunta(data_pub=tempo)
        self.assertIs(p.publicada_recentemente(), False)

    def test_publicada_recentemente_pergunta_no_passado(self):
        """
        O método para pergunta no futuro DEVE retornar False
        """
        tempo = timezone.now() - datetime.timedelta(hours=24,seconds=1)
        p = Pergunta(data_pub=tempo)
        self.assertIs(p.publicada_recentemente(), False)

    def test_publicada_recentemente_pergunta_recente(self):
        """
        O método para pergunta no futuro DEVE retornar True
        """
        tempo = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        p = Pergunta(data_pub=tempo)
        self.assertIs(p.publicada_recentemente(), True)