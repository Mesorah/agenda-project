from django.shortcuts import render
from authors.form import RegisterForm
from django.urls import reverse
from django.contrib import messages


def register_author(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Fazer todos os tests agora
            messages.success(request, 'sucesso!')
    else:
        form = RegisterForm()

    url_action = reverse('authors:register_author')

    return render(request, 'global/pages/base_page.html', context={
        'form': form,
        'title': 'Register',
        'msg': 'Register',
        'url_action': url_action,
    })
