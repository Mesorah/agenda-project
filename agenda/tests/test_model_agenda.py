from django.test import TestCase
from agenda.models import Category, Contact
from django.contrib.auth.models import User
from django.urls import reverse


class CreateModel(TestCase):
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

        return super().setUp()

    def create_category(self, name='Familia'):
        category = Category.objects.create(name=name)

        return category

    def create_user(self, username='Gabriel', password='ABcd12!@$5'):
        user = User.objects.create(
            username=username,
            password=password
        )

        return user

    def create_contact(self,
                       first_name='Gabriel',
                       last_name='Rodrigues',
                       phone='999884734',
                       email='gabrielcambara123@gmail.com',
                       description='Top!',
                       category='Familia'):

        return Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            description=description,
            category=self.create_category(name='Familia')
        )


class TestModelCategoryAgenda(CreateModel):
    def setUp(self):
        self.category = self.create_category()

        return super().setUp()

    def test_category_retuns_correct_name(self):
        self.assertEqual(str(self.category), self.category.name)


class TestModelContactAgenda(CreateModel):
    def setUp(self):
        self.contact = self.create_contact()

        return super().setUp()

    def test_contact_retuns_correct_name(self):
        completed_name = f'{self.contact.first_name} {self.contact.last_name}'

        self.assertEqual(str(self.contact), completed_name)
