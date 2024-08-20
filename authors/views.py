from django.shortcuts import render, redirect
from authors.form import RegisterForm, LoginForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register_author(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Success! Your account has been successfully created.') # noqa E501
            return redirect(reverse('authors:login_author') + f"?username={user.username}") # noqa E501
    else:
        form = RegisterForm()

    url_action = reverse('authors:register_author')

    return render(request, 'global/pages/base_page.html', context={
        'form': form,
        'title': 'Register',
        'msg': 'Register',
        'url_action': url_action,
        'have_account': True
    })


def login_author(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Success! You have been logged in')
                return redirect('agenda:home')
            else:
                messages.error(request, 'Username or password is not correct')

    else:
        initial_data = {
            'username': request.GET.get('username', ''),
        }
        form = LoginForm(initial=initial_data)

    url_action = reverse('authors:login_author')

    return render(request, 'global/pages/base_page.html', context={
        'form': form,
        'title': 'Login',
        'msg': 'Login',
        'url_action': url_action,
        'dont_have_account': True,
    })


def logout_author(request):
    logout(request)

    messages.success(request, 'Success! You have been logged out.')

    return redirect('authors:login_author')
