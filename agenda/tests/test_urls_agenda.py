from django.test import TestCase
from django.urls import reverse, resolve
from agenda import views
from agenda.tests.test_model_agenda import CreateModel
from agenda.models import Category
from django.contrib.auth.models import User


class TestHomeUrlsAgenda(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Gabriel', password='ABcd12!@$5')

        logged_in = self.client.login(
            username='Gabriel', password='ABcd12!@$5')
        self.assertTrue(logged_in, "Login falhou.")

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
        self.assertIs(url.func.view_class, views.ListViewHome)


class TestViewContactUrlsAgenda(CreateModel):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Gabriel', password='ABcd12!@$5')

        logged_in = self.client.login(
            username='Gabriel', password='ABcd12!@$5')
        self.assertTrue(logged_in, "Login falhou.")

        self.contact = self.create_contact()

        return super().setUp()

    def test_view_contact_url_return_status_code_200(self):
        url = self.client.get(reverse('agenda:view_contact',
                                      kwargs={'pk': self.contact.pk}))
        self.assertEqual(url.status_code, 200)

    def test_view_contact_url_load_correct_template(self):
        url = self.client.get(reverse('agenda:view_contact',
                                      kwargs={'pk': self.contact.pk}))
        self.assertTemplateUsed(url, 'agenda/pages/view_contact.html')

    def test_view_contact_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('agenda:view_contact', kwargs={'pk': self.contact.pk})
            ).content.decode('utf-8')
        self.assertIn('View contact', url)

    def test_view_contact_url_load_correct_function(self):
        url = resolve(reverse('agenda:view_contact', kwargs={'pk': 1}))
        self.assertIs(url.func.view_class, views.DetalViewContact)


class TestAddContactUrlsAgenda(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Gabriel', password='ABcd12!@$5')

        logged_in = self.client.login(
            username='Gabriel', password='ABcd12!@$5')
        self.assertTrue(logged_in, "Login falhou.")

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
        self.assertIs(url.func.view_class, views.ContactCreateView)


class TestUpdateContactUrlsAgenda(CreateModel):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Gabriel', password='ABcd12!@$5')

        logged_in = self.client.login(
            username='Gabriel', password='ABcd12!@$5')
        self.assertTrue(logged_in, "Login falhou.")

        self.contact = self.create_contact()

        return super().setUp()

    def test_update_url_return_status_code_200(self):
        response = self.client.post(
            reverse('agenda:update_contact', kwargs={'pk': self.contact.pk}))
        self.assertEqual(response.status_code, 200)

    def test_update_url_return_status_code_302(self):
        response = self.client.post(
            reverse('agenda:update_contact', kwargs={'pk': self.contact.pk}),
            {
                'first_name': 'Gabriel',
                'last_name': 'Rodrigues',
                'phone': '999884734',
                'email': 'gabrielcambara123@gmail.com',
                'description': 'Updated!',
                'category': self.contact.category.pk
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_update_url_load_correct_template(self):
        url = self.client.get(
            reverse('agenda:update_contact', kwargs={'pk': self.contact.pk}))
        self.assertTemplateUsed(url, 'global/pages/base_page.html')

    def test_update_url_template_contain_certaly_word(self):
        url = self.client.get(
            reverse('agenda:update_contact',
                    kwargs={'pk': self.contact.pk})).content.decode('utf-8')
        self.assertIn('<h2>Profile</h2>', url)

    def test_update_url_load_correct_function(self):
        url = resolve(reverse('agenda:update_contact',
                              kwargs={'pk': self.contact.pk}))
        self.assertIs(url.func.view_class, views.ContactUpdateView)


class TestAddCategoryUrlsAgenda(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Gabriel', password='ABcd12!@$5')

        logged_in = self.client.login(
            username='Gabriel', password='ABcd12!@$5')
        self.assertTrue(logged_in, "Login falhou.")

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
        self.assertIs(url.func.view_class, views.CategoryCreateView)


class TestRemoveCategoryUrlsAgenda(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Gabriel', password='ABcd12!@$5')

        logged_in = self.client.login(
            username='Gabriel', password='ABcd12!@$5')
        self.assertTrue(logged_in, "Login falhou.")

        self.category = Category.objects.create(
            name='Test Category', user=self.user
        )

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
        self.assertIs(url.func.view_class, views.CategoryDeleteView)


class TestUpdateCategoryUrlsAgenda(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='Gabriel', password='ABcd12!@$5')

        logged_in = self.client.login(
            username='Gabriel', password='ABcd12!@$5')
        self.assertTrue(logged_in, "Login falhou.")

        self.category = Category.objects.create(
            name='Test Category', user=self.user
        )

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
        self.assertIs(url.func.view_class, views.CategoryUpdateView)
