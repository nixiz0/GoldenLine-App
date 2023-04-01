from django.test import TestCase, Client
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import render
import unittest


class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass1')

    def test_valid_credentials(self):
        response = self.client.post('/login/', {'username': 'user1', 'password': 'pass1'})
        self.assertRedirects(response, reverse('analyse'))  # On redirige l'utilisateur vers la page data-analyse après l'authentification

    def test_invalid_credentials(self):
        response = self.client.post('/login/', {'username': 'user1', 'password': 'abcd4'})
        form = AuthenticationForm()
        error_message = form.errors
        self.assertContains(response, error_message, status_code=200)


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')

    def test_login_page(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


class TestAccess(TestCase):
    def setUp(self):
        self.client = Client()
        self.public_url = reverse('login')
        self.private_url = reverse('analyse')
        self.username = 'user2'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
        )

    def test_public_route_accessible(self):
        response = self.client.get(self.public_url)
        self.assertEqual(response.status_code, 200)

    def test_private_route_not_accessible_unauthenticated(self):
        response = self.client.get(self.private_url)
        self.assertEqual(response.status_code, 302)

    def test_private_route_accessible_authenticated(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.private_url)
        self.assertEqual(response.status_code, 200)
