from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url_ativos = reverse('ativos-list')
        self.list_url_movimentacoes = reverse('movimentacoes-list')
        self.url_saldo = reverse('saldo')
        self.user = User.objects.create_user('test_user', password='123test123')

    def test_autenticando_usuario_e_suas_credenciais(self):
        """ Teste para autenticar um usuário que informa corretamente suas credenciais """
        user = authenticate(username='test_user', password='123test123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao_username_incorreto(self):
        """ Teste para autenticar um usuário que informa erroneamente seu username """
        user = authenticate(username='testuser', password='123test123')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_senha_incorreta(self):
        """ Teste para autenticar um usuário que informa erroneamente sua senha """
        user = authenticate(username='test_user', password='12123')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada_urls_ativos(self):
        """ Teste para realizar uma requisição GET sem autenticação nas urls do Ativo """
        user = authenticate(username='test_user', password='12123')
        response = self.client.get(self.list_url_ativos)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_requisicao_post_nao_autorizada_urls_ativos(self):
        """ Teste para realizar uma requisição POST sem autenticação nas urls do Ativo """
        user = authenticate(username='test_user', password='12123')
        response = self.client.post(self.list_url_ativos)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_requisicao_get_nao_autorizada_urls_movimentacao(self):
        """ Teste para realizar uma requisição GET sem autenticação nas urls do Movimentação """
        user = authenticate(username='test_user', password='12123')
        response = self.client.get(self.list_url_movimentacoes)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_requisicao_post_nao_autorizada_urls_movimentacao(self):
        """ Teste para realizar uma requisição POST sem autenticação nas urls do Movimentação """
        user = authenticate(username='test_user', password='12123')
        response = self.client.post(self.list_url_movimentacoes)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_requisicao_get_autorizada_urls_ativos(self):
        """ Teste para realizar uma requisição GET com autenticação nas urls do Ativo """
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url_ativos)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_autorizada_urls_ativos(self):
        """
        Teste para realizar uma requisição POST com autenticação nas urls do Ativo
        Retornará erro devido à obrigatoriedade de preenchimento de campos
        """
        self.client.force_authenticate(self.user)
        response = self.client.post(self.list_url_ativos)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_requisicao_get_autorizada_urls_movimentacao(self):
        """ Teste para realizar uma requisição GET com autenticação nas urls do Movimentacao """
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url_movimentacoes)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_autorizada_urls_movimentacao(self):
        """
        Teste para realizar uma requisição POST com autenticação nas urls de Movimentações
        Retornará erro devido à obrigatoriedade de preenchimento de campos
        """
        self.client.force_authenticate(self.user)
        response = self.client.post(self.list_url_movimentacoes)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_requisicao_put_autorizada_urls_movimentacao(self):
        """ Teste para realizar uma requisição PUT com autenticação nas urls do movimentacao """
        self.client.force_authenticate(self.user)
        response = self.client.put(self.list_url_movimentacoes)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_requisicao_delete_autorizada_urls_movimentacao(self):
        """ Teste para realizar uma requisição DELETE com autenticação nas urls do movimentacao """
        self.client.force_authenticate(self.user)
        response = self.client.delete(self.list_url_movimentacoes)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_requisicao_patch_autorizada_urls_movimentacao(self):
        """ Teste para realizar uma requisição PATCH com autenticação nas urls do movimentacao """
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.list_url_movimentacoes)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_requisicao_get_autorizada_url_saldo(self):
        """
        Teste para realizar uma requisição GET com autenticação nas url de Saldo
        Retornará 404 por não haver nenhum registro associado ao usuário do setUP
        """

        self.client.force_authenticate(self.user)
        response = self.client.get(self.url_saldo)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
