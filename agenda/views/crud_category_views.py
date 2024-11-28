from django.shortcuts import render, redirect
from agenda.form import CategoryForm, RemoveCategoryForm, UpdateCategoryForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


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
