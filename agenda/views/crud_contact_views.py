from django.shortcuts import render, redirect, get_object_or_404
from agenda.models import Contact
from agenda.form import ContactForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views import View


class ContactCreateView(CreateView):
    template_name = 'global/pages/base_page.html'
    form_class = ContactForm
    success_url = reverse_lazy('agenda:home')
    prefix = None



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
