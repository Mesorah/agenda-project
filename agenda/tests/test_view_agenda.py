from agenda.tests.test_model_agenda import CreateModel
from agenda.models import Contact, Category
from django.urls import reverse
from django.contrib.auth.models import User


class TestViewAgenda(CreateModel):
    def setUp(self) -> None:
        self.contact = self.create_contact(phone='199884734', email='gabrielcambara124@gmail.com') # noqa E501

        return super().setUp()

    def test_if_contact_is_deleted(self):
        self.contact1 = self.create_contact(phone='199884734', email='gabrielcambara124@gmail.com') # noqa E501
        self.contact2 = self.create_contact(phone='299884734', email='gabrielcambara125@gmail.com') # noqa E501
        self.contact3 = self.create_contact(phone='399884734', email='gabrielcambara126@gmail.com') # noqa E501

        before = list(Contact.objects.all())

        self.contact1.delete()

        after = list(Contact.objects.all())

        self.assertNotEqual(before, after)

    def test_remove_contact(self):
        url = reverse('agenda:remove_contact', kwargs={'id': self.contact.id})
        response = self.client.get(url)

        self.assertEqual(Contact.objects.count(), 0)

        self.assertRedirects(response, reverse('agenda:home'))

    def test_if_request_in_add_contact_is_post(self):
        User.objects.create_user(username='test', password='12345')
        self.client.login(username='test', password='12345')
        category = Category.objects.create(name='Fried')

        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '123456789',
            'email': 'john.doe@example.com',
            'description': 'A test contact',
            'category': category.id,
            'cover': ''
        }

        response = self.client.post(
            reverse('agenda:add_contact'), data=form_data)
        self.assertEqual(response.status_code, 302)

        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '123456789',
            'email': 'john.doe@example.com',
            'description': 'A test contact',
            'category': 'IDK',
            'cover': ''
        }

        response = self.client.post(
            reverse('agenda:add_contact'), data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_if_request_in_add_contact_is_get(self):
        User.objects.create_user(username='test', password='12345')
        self.client.login(username='test', password='12345')
        Category.objects.create(name='Fried')
        Contact.objects.get(id=1)

        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '123456789',
            'email': 'john.doe@example.com',
            'description': 'A test contact',
            'category': 'IDK',
            'cover': ''
        }

        response = self.client.post(
            reverse('agenda:add_contact'), data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_if_request_in_update_contact_is_post(self):
        User.objects.create_user(username='test', password='12345')
        self.client.login(username='test', password='12345')

        contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            phone='123456789',
            email='john.doe@example.com',
            description='A test contact',
            cover=''
        )

        url = reverse('agenda:update_contact', kwargs={'id': contact.id})

        response = self.client.post(url, {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'phone': '987654321',
            'email': 'jane.doe@example.com',
            'description': 'Updated contact',
            'cover': ''
        })

        self.assertEqual(response.status_code, 302)

        response = self.client.post(url, {
            'last_name': 'Doe',
            'phone': '987654321',
            'email': 'jane.doe@example.com',
            'description': 'Updated contact',
            'cover': ''
        })

        self.assertEqual(response.status_code, 200)

    def test_if_request_in_update_contact_is_get(self):
        User.objects.create_user(username='test', password='12345')
        self.client.login(username='test', password='12345')

        contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            phone='123456789',
            email='john.doe@example.com',
            description='A test contact',
            cover=''
        )

        url = reverse('agenda:update_contact', kwargs={'id': contact.id})

        response = self.client.get(url, {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'phone': '987654321',
            'email': 'jane.doe@example.com',
            'description': 'Updated contact',
            'cover': ''
        })

        self.assertEqual(response.status_code, 200)
