from authors.form import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class AuthorRegisterView(FormView):
    template_name = 'global/pages/base_page.html'
    form_class = RegisterForm
    success_url = reverse_lazy('agenda:home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Register',
            'msg': 'Register',
        })

        return context

    def form_valid(self, form):
        form.save()

        return redirect(self.success_url)


class AuthorLoginView(LoginView):
    template_name = 'global/pages/base_page.html'
    success_url = reverse_lazy('agenda:home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context.update({
            'title': 'Login',
            'msg': 'Login',
            'dont_have_account': True,
        })

        return context

    def get_success_url(self):
        return self.success_url


class AuthorLogoutView(LoginRequiredMixin, LogoutView):
    login_url = 'authors:login_author'

    def get_redirect_url(self):
        return '/'
