from django.shortcuts import get_object_or_404
from agenda.form import CategoryForm, RemoveCategoryForm, UpdateCategoryForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from agenda.models import Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    login_url = 'authors:login_author'
    template_name = 'global/pages/base_page.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('agenda:home')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Add Category',
            'msg': 'Category',
        })

        return context


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'authors:login_author'
    template_name = 'global/pages/base_page.html'
    model = Category
    form_class = UpdateCategoryForm
    success_url = reverse_lazy('agenda:home')

    def get_object(self, queryset=None):
        return get_object_or_404(Category, user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passa o user para o formulário
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Update Category',
            'msg': 'Update Category',
        })

        return context


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'authors:login_author'
    template_name = 'global/pages/base_page.html'
    model = Category
    form_class = RemoveCategoryForm
    success_url = reverse_lazy('agenda:home')

    def get_object(self, queryset=None):
        return get_object_or_404(Category, user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Remove Category',
            'msg': 'Remove Category',
        })

        return context
