from django.shortcuts import render, redirect, get_object_or_404
from agenda.models import Contact
from agenda.form import ContactForm, CategoryForm, RemoveCategoryForm, UpdateCategoryForm  # noqa E501
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class ListViewBase(ListView):
    template_name = 'agenda/pages/home.html'
    model = Contact
    paginate_by = 2
    context_object_name = 'contacts'
    paginator_class = Paginator

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(
            user=self.request.user
        ).order_by('-id')

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Home',
            'user': self.request.user
        })

        return context


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class ListViewHome(ListViewBase):
    template_name = 'agenda/pages/home.html'


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class ListViewSearch(ListViewBase):
    template_name = 'agenda/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        search_term = self.request.GET.get('q', '').strip()

        queryset = queryset.filter(
            Q(user=self.request.user) & (
                Q(id__icontains=search_term) |
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(phone__icontains=search_term) |
                Q(email__icontains=search_term)
            )
        ).order_by('-id')

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '').strip()

        context.update({
            'search_term': search_term,
            'title': 'Search'
        })

        return context


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class DetalViewContact(DetailView):
    template_name = 'agenda/pages/view_contact.html'
    model = Contact
    context_object_name = 'contact'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        queryset = queryset.filter(
            pk=self.kwargs.get('pk'),
            user=self.request.user
        )

        return queryset


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class AddUpdateContact(View):
    def get_context(self, form, title, url_action=''):
        return render(self.request, 'global/pages/base_page.html', context={
            'form': form,
            'title': title,
            'msg': 'Profile',
            'url_action': url_action,
        })

    def _if_id_is_true(self, id):
        contact = get_object_or_404(Contact, id=id, user=self.request.user)
        title = 'Update contact'
        url_action = reverse('agenda:update_contact', args=[id])

        return contact, title, url_action

    def _if_id_is_false(self):
        contact = None
        title = 'Add contact'
        url_action = reverse('agenda:add_contact')

        return contact, title, url_action

    def get_elements(self, id):
        if id:
            return self._if_id_is_true(id)

        return self._if_id_is_false()

    def get(self, request, id=None):
        contact, title, url_action = self.get_elements(id)

        form = ContactForm(user=self.request.user, instance=contact)

        return self.get_context(form, title, url_action)

    def post(self, request, id=None):
        contact, title, url_action = self.get_elements(id)

        form = ContactForm(request.POST,
                           request.FILES,
                           user=self.request.user,
                           instance=contact
                           )

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = self.request.user
            contact.save()

            messages.success(request, 'Contact added successfully!')

            return redirect('agenda:home')

        return self.get_context(form, title, url_action)


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class RemoveContactView(View):
    def post(self, request, id):
        contact = get_object_or_404(Contact, id=id, user=self.request.user)
        contact.delete()

        messages.success(request, 'Contact successfully removed!')

        return redirect('agenda:home')


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class AddCategoryView(View):
    def get_context(self, form, title, url_action=''):
        return render(self.request, 'global/pages/base_page.html', context={
            'form': form,
            'title': title,
            'msg': 'Category',
            'url_action': url_action,
        })

    def get(self, request):
        form = CategoryForm()

        return self.get_context(form,
                                'Add category',
                                reverse('agenda:add_category')
                                )

    def post(self, request):
        form = CategoryForm(self.request.POST, self.request.FILES)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Category added successfully!')
            return redirect('agenda:add_contact')


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class UpdateCategoryView(View):
    def get_context(self, form, title, url_action=''):
        return render(self.request, 'global/pages/base_page.html', context={
            'form': form,
            'title': title,
            'msg': 'Category',
            'url_action': url_action,
        })

    def get(self, request):
        form = UpdateCategoryForm()

        return self.get_context(form,
                                'Update category',
                                reverse('agenda:update_category')
                                )

    def post(self, request):
        form = UpdateCategoryForm(self.request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']
            new_name = form.cleaned_data['new_name']
            category.name = new_name
            category.save()
            messages.success(request, 'Category Successfully Changed!')

            return redirect('agenda:add_contact')

        return self.get_context(form,
                                'Update category',
                                reverse('agenda:update_category')
                                )


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class RemoveCategoryView(View):
    def get_context(self, form, title, url_action=''):
        return render(self.request, 'global/pages/base_page.html', context={
            'form': form,
            'title': title,
            'msg': 'Remove category',
            'url_action': url_action,
        })

    def get(self, request):
        form = RemoveCategoryForm()

        return self.get_context(form,
                                'Remove category',
                                reverse('agenda:remove_category')
                                )

    def post(self, request):
        form = RemoveCategoryForm(self.request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']
            category.delete()
            messages.success(self.request, 'Category successfully removed!')
            return redirect('agenda:add_contact')

        return self.get_context(form,
                                'Remove category',
                                reverse('agenda:remove_category')
                                )
