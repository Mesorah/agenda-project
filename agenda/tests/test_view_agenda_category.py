from agenda.tests.test_model_agenda import CreateModel
from django.urls import reverse


class TestAddCategory(CreateModel):
    def test_if_request_in_add_category_is_post(self):
        form_data = {
            'name': 'Family'
        }

        response = self.client.post(
            reverse('agenda:add_category'), data=form_data)
        self.assertEqual(response.status_code, 302)


class TestRemoveCategory(CreateModel):
    def test_if_request_in_remove_category_is_post(self):
        category = self.create_category()

        response = self.client.post(
            reverse('agenda:remove_category'), {'category': category.pk})
        self.assertEqual(response.status_code, 302)


class TestUpdateCategory(CreateModel):
    def test_if_request_in_update_category_is_post(self):
        category = self.create_category()

        url = reverse('agenda:update_category')

        response = self.client.post(url, {'category': category.id,
                                          'new_name': 'TESTING'})
        self.assertEqual(response.status_code, 302)

    def test_if_request_in_add_category_is_get(self):
        form_data = {
            'name': 'Family'
        }

        response = self.client.get(
            reverse('agenda:add_category'), data=form_data)
        self.assertEqual(response.status_code, 302)
