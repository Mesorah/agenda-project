from django.shortcuts import render, redirect
from authors.form import RegisterForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class AuthorRegisterView(FormView):
    template_name = 'global/pages/base_page.html'
    form_class = RegisterForm
    success_url = reverse_lazy('agenda:home')

    def form_valid(self, form):
        user = form.save()

        login(self.request, user)

        return super().form_valid(form)


class RegisterAuthorView(View):
    def get_context(self, form):
        return render(self.request, 'global/pages/base_page.html', context={
            'form': form,
            'title': 'Register',
            'msg': 'Register',
            'url_action': reverse('authors:register_author'),
            'have_account': True
        })

    def get(self, request):
        form = RegisterForm()

        return self.get_context(form)

    def post(self, request):
        form = RegisterForm(self.request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(
                self.request,
                'Success! Your account has been successfully created.'
                )

            return redirect(
                reverse('authors:login_author') + f"?username={user.username}"
                )

        return self.get_context(form)


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


@method_decorator(
    login_required(login_url='authors:login_author', redirect_field_name='next'), # noqa E501
    name='dispatch'
)
class AuthorLogoutView(LogoutView):
    def get_redirect_url(self):
        return '/'
