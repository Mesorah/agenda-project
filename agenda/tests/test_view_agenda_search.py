from agenda.tests.test_model_agenda import CreateModel
from django.urls import reverse
from django.contrib.auth.models import User


class TestSearch(CreateModel):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Gabriel', password='ABcd12!@$5')

        logged_in = self.client.login(
            username='Gabriel', password='ABcd12!@$5')
        self.assertTrue(logged_in, "Login falhou.")

        return super().setUp()

    def test_if_search_does_not_exists(self):
        url = self.client.get(
            reverse('agenda:search') + '?q=test').content.decode('utf-8')
        self.assertIn('<p>Search not found</p>', url)

    def test_if_search_exists(self):
        self.create_contact()

        url = self.client.get(
            reverse('agenda:search') + '?q=Gabriel').content.decode('utf-8')
        self.assertNotIn('<p>Search not found</p>', url)
