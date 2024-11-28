from django.shortcuts import render, redirect
from authors.form import RegisterForm, LoginForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View


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


class LoginAuthorView(View):
    def get_context(self, form):
        return render(self.request, 'global/pages/base_page.html', context={
            'form': form,
            'title': 'Login',
            'msg': 'Login',
            'url_action': reverse('authors:login_author'),
            'dont_have_account': True,
        })

    def get(self, request):
        initial_data = {
            'username': request.GET.get('username', ''),
        }

        form = LoginForm(initial=initial_data)

        return self.get_context(form)

    def post(self, request):
        form = LoginForm(self.request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(self.request, user)
                messages.success(
                    self.request,
                    'Success! You have been logged in'
                    )

                return redirect('agenda:home')

            messages.error(
                self.request,
                'Username or password is not correct'
                )


class LogoutAuthorView(View):
    def post(self, request):
        logout(request)

        messages.success(
            self.request,
            'Success! You have been logged out.'
            )

        return redirect('authors:login_author')
