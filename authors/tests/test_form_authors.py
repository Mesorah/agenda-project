from django.urls import reverse
from django.test import TestCase
from authors.form import LoginForm


class TestRegisterForm(TestCase):
    def setUp(self):
        self.form_data = {
            'username': 'JohnDoe',
            'first_name': 'Johny',
            'last_name': 'Doeny',
            'email': 'john.doe@example.com',
            'password': '!@33dfDFG!2d',
            'confirm_password': '!@33dfDFG!2d',
        }
        return super().setUp()

    def test_if_username_and_email_exists(self):
        # Create
        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 302)

        # ERROR
        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 200)

    def test_if_password_is_not_strong(self):
        self.form_data['password'] = '123'
        self.form_data['confirm_password'] = '123'

        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 200)

        form = response.context.get('form')
        self.assertIn('password', form.errors)

        error_message = form.errors['password'][0]
        self.assertIn(
            'Password must be at least 8 characters long',
            error_message
        )

    def test_if_password_is_empty(self):
        self.form_data['password'] = ''
        self.form_data['confirm_password'] = ''

        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn('password', form.errors)
        self.assertEqual(form.errors['password'], ['This field is required.'])

    def test_if_password_is_none(self):
        self.form_data.pop('password')
        self.form_data.pop('confirm_password')

        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 200)

        form = response.context['form']

        self.assertIn('password', form.errors)
        self.assertEqual(form.errors['password'], ['This field is required.'])

    def test_if_passoword_is_valid(self):
        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 302)

        if response.status_code == 200:
            form = response.context.get('form')
            self.assertNotIn('password', form.errors)

    def test_if_password_and_confirm_password_is_not_equal(self):
        self.form_data['password'] = '123'

        response = self.client.post(
            reverse('authors:register_author'), data=self.form_data)
        self.assertEqual(response.status_code, 200)


class TestLoginForm(TestCase):
    def setUp(self):
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

        return super().setUp()

    def test_form_with_missing_username(self):
        login_data = {
            'username': '',
            'password': '!@33dfDFG!2d',
        }

        form = LoginForm(data=login_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('This field is required.', form.errors['username'])

    def test_form_with_missing_password(self):
        login_data = {
            'username': 'JohnDoe',
            'password': '',
        }

        form = LoginForm(data=login_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertIn('This field is required.', form.errors['password'])

    def test_form_with_missing_username_and_password(self):
        login_data = {
            'username': '',
            'password': '',
        }

        form = LoginForm(data=login_data)
        self.assertFalse(form.is_valid())

        self.assertIn('username', form.errors)
        self.assertIn('This field is required.', form.errors['username'])

        self.assertIn('password', form.errors)
        self.assertIn('This field is required.', form.errors['password'])

    def test_form_with_has_valid_username_and_password(self):
        login_data = {
            'username': 'JohnDoe',
            'password': '!@33dfDFG!2d',
        }

        form = LoginForm(data=login_data)
        self.assertTrue(form.is_valid())

        self.assertEqual(form.cleaned_data['username'], 'JohnDoe')
        self.assertEqual(form.cleaned_data['password'], '!@33dfDFG!2d')
