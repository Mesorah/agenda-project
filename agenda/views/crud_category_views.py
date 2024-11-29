from django.shortcuts import get_object_or_404
from agenda.form import CategoryForm, RemoveCategoryForm, UpdateCategoryForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from agenda.models import Category


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class CategoryCreateView(CreateView):
    template_name = 'global/pages/base_page.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('agenda:home')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class CategoryUpdateView(UpdateView):
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


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class CategoryDeleteView(DeleteView):
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
