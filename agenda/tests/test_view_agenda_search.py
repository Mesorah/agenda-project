from agenda.tests.test_model_agenda import CreateModel
from django.urls import reverse


class TestSearch(CreateModel):
    def test_if_search_does_not_exists(self):
        url = self.client.get(
            reverse('agenda:search') + '?q=test').content.decode('utf-8')
        self.assertIn('<p>Search not found</p>', url)

    def test_if_search_exists(self):
        self.create_contact()
        url = self.client.get(
            reverse('agenda:search') + '?q=Gabriel').content.decode('utf-8')
        self.assertNotIn('<p>Search not found</p>', url)
