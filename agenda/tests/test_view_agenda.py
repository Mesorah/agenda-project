from agenda.tests.test_model_agenda import CreateModel
from agenda.models import Contact
from django.urls import reverse


class TestViewAgenda(CreateModel):
    def setUp(self) -> None:
        self.contact = self.create_contact(phone='199884734', email='gabrielcambara124@gmail.com') # noqa E501

        return super().setUp()

    def test_if_contact_is_deleted(self):
        self.contact1 = self.create_contact(phone='199884734', email='gabrielcambara124@gmail.com') # noqa E501
        self.contact2 = self.create_contact(phone='299884734', email='gabrielcambara125@gmail.com') # noqa E501
        self.contact3 = self.create_contact(phone='399884734', email='gabrielcambara126@gmail.com') # noqa E501

        antes = list(Contact.objects.all())

        self.contact1.delete()

        depois = list(Contact.objects.all())

        self.assertNotEqual(antes, depois)

    def test_remove_contact(self):
        url = reverse('agenda:remove_contact', kwargs={'id': self.contact.id})
        response = self.client.get(url)

        self.assertEqual(Contact.objects.count(), 0)

        self.assertRedirects(response, reverse('agenda:home'))
