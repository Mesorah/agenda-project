from django.test import TestCase
from django.urls import reverse, resolve
from agenda import views
from agenda.tests.test_model_agenda import CreateModel


class TestHomeUrlsAgenda(TestCase):
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


# Arrumar todos os tests

class TestViewContactUrlsAgenda(CreateModel):
    def test_view_contact_url_return_status_code_200(self):
        contact = self.create_contact()
        url = self.client.get(reverse('agenda:view_contact', kwargs={'id': contact.id}))
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


class TestAddContactUrlsAgenda(TestCase):
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

    def test_add_url_return_status_code_200(self):
        url = self.client.get(reverse('agenda:add_contact'))
        self.assertEqual(url.status_code, 200)

    def test_add_url_load_correct_template(self):
        url = self.client.get(reverse('agenda:add_contact'))
        self.assertTemplateUsed(url, 'global/pages/base_page.html')

    def test_add_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('agenda:add_contact')).content.decode('utf-8')
        self.assertIn('<h2>Profile</h2>', url)

    def test_add_url_load_correct_function(self):
        url = resolve(reverse('agenda:add_contact'))
        self.assertIs(url.func, views.add_contact)


class TestUpdateContactUrlsAgenda(TestCase):
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


class TestAddCategoryUrlsAgenda(TestCase):
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

    def test_add_category_url_return_status_code_200(self):
        url = self.client.get(reverse('agenda:add_category'))
        self.assertEqual(url.status_code, 200)

    def test_add_category_url_load_correct_template(self):
        url = self.client.get(reverse('agenda:add_category'))
        self.assertTemplateUsed(url, 'global/pages/base_page.html')

    def test_add_category_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('agenda:add_category')).content.decode('utf-8')
        self.assertIn('<h2>Category</h2>', url)

    def test_add_category_url_load_correct_function(self):
        url = resolve(reverse('agenda:add_category'))
        self.assertIs(url.func, views.add_category)


class TestRemoveCategoryUrlsAgenda(TestCase):
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

    def test_remove_category_url_return_status_code_200(self):
        url = self.client.get(reverse('agenda:remove_category'))
        self.assertEqual(url.status_code, 200)

    def test_remove_category_url_load_correct_template(self):
        url = self.client.get(reverse('agenda:remove_category'))
        self.assertTemplateUsed(url, 'global/pages/base_page.html')

    def test_remove_category_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('agenda:remove_category')).content.decode('utf-8')
        self.assertIn('<h2>Remove Category</h2>', url)

    def test_remove_category_url_load_correct_function(self):
        url = resolve(reverse('agenda:remove_category'))
        self.assertIs(url.func, views.remove_category)


class TestUpdateCategoryUrlsAgenda(TestCase):
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

    def test_update_category_url_return_status_code_200(self):
        url = self.client.get(reverse('agenda:update_category'))
        self.assertEqual(url.status_code, 200)

    def test_update_category_url_load_correct_template(self):
        url = self.client.get(reverse('agenda:update_category'))
        self.assertTemplateUsed(url, 'global/pages/base_page.html')

    def test_update_category_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('agenda:update_category')).content.decode('utf-8')
        self.assertIn('<h2>Update Category</h2>', url)

    def test_update_category_url_load_correct_function(self):
        url = resolve(reverse('agenda:update_category'))
        self.assertIs(url.func, views.update_category)
