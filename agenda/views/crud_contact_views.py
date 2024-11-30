from agenda.models import Contact
from agenda.form import ContactForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class ContactViewSettingsMixin(LoginRequiredMixin):
    login_url = 'authors:login_author'
    template_name = 'global/pages/base_page.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('agenda:home')


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


class ContactUpdateView(ContactViewSettingsMixin, UpdateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Update Contact',
            'msg': 'Profile',
        })

        return context


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'authors:login_author'
    model = Contact
    template_name = None
    success_url = reverse_lazy('agenda:home')

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.success_url)
