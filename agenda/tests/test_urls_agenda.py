from django.test import TestCase
# from unittest import TestCase
from django.urls import reverse, resolve
from agenda import views
from agenda.tests.test_model_agenda import CreateModel


class TestHomeUrlsAgenda(TestCase):
    # Home
    def test_home_url_return_status_code_200(self):
        url = self.client.get(reverse('agenda:home'))
        self.assertEqual(url.status_code, 200)

    def test_home_url_load_correct_template(self):
        url = self.client.get(reverse('agenda:home'))
        self.assertTemplateUsed(url, 'agenda/pages/home.html')

    def test_home_url_template_contain_certaly_word(self):
        url = self.client.get(reverse('agenda:home')).content.decode('utf-8')
        self.assertIn('Home', url)

    def test_home_url_load_correct_function(self):
        url = resolve(reverse('agenda:home'))
        self.assertIs(url.func, views.home)

    # view_contact
    def test_view_contact_url_return_status_code_200(self):
        url = self.client.get(reverse('agenda:view_contact', kwargs={'id': 1}))
        self.assertEqual(url.status_code, 200)

    def test_view_contact_url_load_correct_template(self):
        url = self.client.get(reverse('agenda:view_contact', kwargs={'id': 1}))
        self.assertTemplateUsed(url, 'agenda/pages/view_contact.html')

    def test_view_contact_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('agenda:view_contact', kwargs={'id': 1})
            ).content.decode('utf-8')
        self.assertIn('View contact', url)

    def test_view_contact_url_load_correct_function(self):
        url = resolve(reverse('agenda:view_contact', kwargs={'id': 1}))
        self.assertIs(url.func, views.view_contact)

    # Add
    def test_add_url_return_status_code_200(self):
        url = self.client.get(reverse('agenda:add_contact'))
        self.assertEqual(url.status_code, 200)

    def test_add_url_load_correct_template(self):
        url = self.client.get(reverse('agenda:add_contact'))
        self.assertTemplateUsed(url, 'agenda/pages/add_contact.html')

    def test_add_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('agenda:add_contact')).content.decode('utf-8')
        self.assertIn('<h2>Profile</h2>', url)

    def test_add_url_load_correct_function(self):
        url = resolve(reverse('agenda:add_contact'))
        self.assertIs(url.func, views.add_contact)

    # Update
    def test_update_url_return_status_code_200(self):
        CreateModel().create_contact()
        url = self.client.get(
            reverse('agenda:update_contact', kwargs={'id': 1}))
        self.assertEqual(url.status_code, 200)

    def test_update_url_load_correct_template(self):
        CreateModel().create_contact()
        url = self.client.get(
            reverse('agenda:update_contact', kwargs={'id': 1}))
        self.assertTemplateUsed(url, 'agenda/pages/update_contact.html')

    def test_update_url_template_contain_certaly_word(self):
        CreateModel().create_contact()
        url = self.client.get(
            reverse('agenda:update_contact',
                    kwargs={'id': 1})).content.decode('utf-8')
        self.assertIn('<h2>Profile</h2>', url)

    def test_update_url_load_correct_function(self):
        CreateModel().create_contact()
        url = resolve(reverse('agenda:update_contact', kwargs={'id': 1}))
        self.assertIs(url.func, views.update_contact)
