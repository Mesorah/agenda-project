from agenda.models import Contact
from agenda.form import ContactForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect


class ContactViewSettingsMixin:
    template_name = 'global/pages/base_page.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('agenda:home')


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class ContactCreateView(ContactViewSettingsMixin, CreateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Category',
            'msg': 'Profile',
        })

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class ContactUpdateView(ContactViewSettingsMixin, UpdateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Update Contact',
            'msg': 'Profile',
        })

        return context


@method_decorator(
    login_required(login_url='authors:login_author'),
    name='dispatch'
)
class ContactDeleteView(DeleteView):
    model = Contact
    template_name = None
    success_url = reverse_lazy('agenda:home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.success_url)
