from django.urls import reverse
from django.test import TestCase


class TestRegisterAuthor(TestCase):
    def test_if_request_in_register_author_is_post(self):
        form_data = {
            'username': 'JohnDoe',
            'first_name': 'Johny',
            'last_name': 'Doeny',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'confirm_password': '!@33dfDFG!2d',
        }

        response = self.client.post(
            reverse('authors:register_author'), data=form_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(
            reverse('authors:register_author'))
        self.assertEqual(response.status_code, 200)

    def test_if_request_in_register_author_is_get(self):
        form_data = {
            'username': 'JohnDoe',
            'first_name': 'Johny',
            'last_name': 'Doeny',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'confirm_password': '!@33dfDFG!2d',
        }

        response = self.client.get(
            reverse('authors:register_author'), data=form_data)
        self.assertEqual(response.status_code, 200)


class TestLoginAuthor(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'username': 'Messorah',
            'first_name': 'Gabriel',
            'last_name': 'Rodrigues',
            'email': 'gabrielcambara556@gmail.com',
            'password': 'TTeessttee11!!',
            'confirm_password': 'TTeessttee11!!',
        }

        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(
            reverse('authors:logout_author')
        )
        self.assertEqual(response.status_code, 302)

        return super().setUp()

    def test_if_request_in_login_author_is_post(self):
        login_data = {
            'username': 'Messorah',
            'password': 'TTeessttee11!!',
        }

        response = self.client.post(
            reverse('authors:login_author'), data=login_data)
        self.assertEqual(response.status_code, 302)

        # response = self.client.post(
        #     reverse('authors:login_author'))
        # self.assertEqual(response.status_code, 200)

    def test_if_request_in_register_author_is_get(self):
        login_data = {
            'username': 'JohnDoe',
            'password': '!@33dfDFG!2d',
        }

        response = self.client.get(
            reverse('authors:register_author'), data=login_data)
        self.assertEqual(response.status_code, 200)

    def test_if_login_user_dont_exists(self):
        login_data = {
            'username': 'Messorah',
            'password': '!@33dfDFG!2d',
        }

        response = self.client.post(
            reverse('authors:login_author'), data=login_data)
        self.assertEqual(response.status_code, 200)


class TestLogoutAuthor(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'username': 'JohnDoe',
            'first_name': 'Johny',
            'last_name': 'Doeny',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'confirm_password': '!@33dfDFG!2d',
        }
        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 302)

        self.login_data = {
            'username': 'JohnDoe',
            'password': '!@33dfDFG!2d',
        }
        response = self.client.post(
            reverse('authors:login_author'), data=self.login_data)
        self.assertEqual(response.status_code, 302)

    def test_logout_user(self):
        response = self.client.post(
            reverse('authors:logout_author'),)
        self.assertEqual(response.status_code, 302)
