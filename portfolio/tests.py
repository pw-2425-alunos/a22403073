from django.test import TestCase, Client
from django.urls import reverse, resolve
from portfolio.models import Projeto, Disciplina, Interesse
from portfolio.views import index_view, interesses_defesa_view
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site


class ModelsTest(TestCase):
    fixtures = ['db.json']

    def test_projeto_str(self):
        projeto = Projeto.objects.first()
        self.assertIsNotNone(projeto, "Nenhum projeto encontrado na fixture.")
        self.assertEqual(str(projeto), projeto.titulo)

    def test_relacionamento_projeto_disciplina(self):
        projeto = Projeto.objects.first()
        self.assertIsNotNone(projeto, "Nenhum projeto encontrado para testar a disciplina.")
        self.assertIsInstance(projeto.disciplina, Disciplina)

    def test_interesse_relacoes(self):
        interesse = Interesse.objects.first()
        self.assertIsNotNone(interesse, "Nenhum interesse encontrado na fixture.")
        self.assertGreaterEqual(interesse.projetos.count(), 0)
        self.assertGreaterEqual(interesse.tecnologias.count(), 0)
        self.assertGreaterEqual(interesse.disciplinas.count(), 0)


class UrlsTest(TestCase):
    def test_url_index_resolve_view(self):
        url = reverse('portfolio:index')
        self.assertEqual(resolve(url).func, index_view)

    def test_url_interesses_defesa_resolve(self):
        url = reverse('portfolio:interesses_defesa')
        self.assertEqual(resolve(url).func, interesses_defesa_view)


class ViewsTest(TestCase):
    fixtures = ['db.json']

    @classmethod
    def setUpTestData(cls):
        site = Site.objects.get_current()
        app = SocialApp.objects.create(
            provider="google",
            name="Google",
            client_id="fake-id",
            secret="fake-secret"
        )
        app.sites.add(site)

    def setUp(self):
        self.client = Client()
