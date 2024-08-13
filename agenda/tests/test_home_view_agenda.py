from django.test import TestCase
# from unittest import TestCase
from django.urls import reverse, resolve
from agenda import views


class TestHomeViewAgenda(TestCase):
    def test_home_view_return_status_code_200(self):
        url = self.client.get(reverse('agenda:home'))
        self.assertEqual(url.status_code, 200)

    def test_home_view_load_correct_template(self):
        url = self.client.get(reverse('agenda:home'))
        self.assertTemplateUsed(url, 'agenda/pages/home.html')

    def test_home_view_template_contain_certaly_word(self):
        url = self.client.get(reverse('agenda:home')).content.decode('utf-8')
        self.assertIn('Home', url)

    def test_home_view_load_correct_function(self):
        url = resolve(reverse('agenda:home'))
        self.assertEqual(url.func, views.home)
