from django.test import TestCase
from django.urls import reverse, resolve
from authors import views


class TestRegisterAuthorUrlsAgenda(TestCase):
    def test_register_form_url_return_status_code_200(self):
        url = self.client.get(reverse('authors:register_author'))
        self.assertEqual(url.status_code, 200)

    def test_register_form_url_load_correct_template(self):
        url = self.client.get(reverse('authors:register_author'))
        self.assertTemplateUsed(url, 'global/pages/base_page.html')

    def test_register_form_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('authors:register_author')).content.decode('utf-8')
        self.assertIn('<h2>Register</h2>', url)

    def test_register_form_url_load_correct_function(self):
        url = resolve(reverse('authors:register_author'))
        self.assertIs(url.func, views.register_author)


class TestLoginAuthorUrlsAgenda(TestCase):
    def test_login_form_url_return_status_code_200(self):
        url = self.client.get(reverse('authors:login_author'))
        self.assertEqual(url.status_code, 200)

    def test_login_form_url_load_correct_template(self):
        url = self.client.get(reverse('authors:login_author'))
        self.assertTemplateUsed(url, 'global/pages/base_page.html')

    def test_login_form_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('authors:login_author')).content.decode('utf-8')
        self.assertIn('<h2>Login</h2>', url)

    def test_login_form_url_load_correct_function(self):
        url = resolve(reverse('authors:login_author'))
        self.assertIs(url.func.view_class, views.AuthorLoginView)
