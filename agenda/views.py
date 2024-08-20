from django.shortcuts import render, redirect, get_object_or_404
from agenda.models import Contact
from agenda.form import ContactForm, CategoryForm, RemoveCategoryForm, UpdateCategoryForm  # noqa E501
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='authors:login_author')
def home(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agenda/pages/home.html', context={
        'contacts': contacts,
        'page_obj': page_obj,
        'var_for': page_obj,
        'title': 'Home',
        'user': request.user
    })


@login_required(login_url='authors:login_author')
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, 'Contact added successfully!')
            return redirect('agenda:home')
    else:
        form = ContactForm()

    url_action = reverse('agenda:add_contact')

    return render(request, 'global/pages/base_page.html', context={
        'form': form,
        'title': 'Add contact',
        'msg': 'Profile',
        'url_action': url_action,
    })


@login_required(login_url='authors:login_author')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('agenda:add_contact')
    else:
        form = CategoryForm()

    url_action = reverse('agenda:add_category')

    return render(request, 'global/pages/base_page.html', context={
        'form': form,
        'title': 'Add category',
        'msg': 'Category',
        'url_action': url_action,
    })


@login_required(login_url='authors:login_author')
def remove_contact(request, id):
    contact = get_object_or_404(Contact, id=id, user=request.user)
    contact.delete()
    messages.success(request, 'Contact successfully removed!')
    return redirect('agenda:home')


@login_required(login_url='authors:login_author')
def remove_category(request):
    if request.method == 'POST':
        form = RemoveCategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            category.delete()
            messages.success(request, 'Category successfully removed!')
            return redirect('agenda:add_contact')
    else:
        form = RemoveCategoryForm()

    url_action = reverse('agenda:remove_category')

    return render(request, 'global/pages/base_page.html', context={
        'form': form,
        'title': 'Remove category',
        'msg': 'Remove Category',
        'url_action': url_action,
    })


@login_required(login_url='authors:login_author')
def update_contact(request, id):
    contact = get_object_or_404(Contact, id=id, user=request.user)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Successfully Changed!')
            return redirect('agenda:home')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'agenda/pages/update_contact.html', context={
        'form': form,
        'contact': contact
    })


@login_required(login_url='authors:login_author')
def update_category(request):
    if request.method == 'POST':
        form = UpdateCategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            new_name = form.cleaned_data['new_name']
            category.name = new_name
            category.save()
            messages.success(request, 'Category Successfully Changed!')

            return redirect('agenda:add_contact')
    else:
        form = UpdateCategoryForm()

    url_action = reverse('agenda:update_category')

    return render(request, 'global/pages/base_page.html', context={
        'form': form,
        'title': 'Update category',
        'msg': 'Update Category',
        'url_action': url_action,
    })


@login_required(login_url='authors:login_author')
def view_contact(request, id):
    contact = get_object_or_404(Contact, id=id, user=request.user)

    return render(request, 'agenda/pages/view_contact.html', context={
        'contact': contact
    })


@login_required(login_url='authors:login_author')
def search(request):
    search_term = request.GET.get('q', '').strip()

    contacts = Contact.objects.filter(
        Q(user=request.user) & (
            Q(id__icontains=search_term) |
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term) |
            Q(phone__icontains=search_term) |
            Q(email__icontains=search_term)
        )
    ).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agenda/pages/home.html', context={
        'contacts': contacts,
        'search_term': search_term,
        'var_for': contacts,
        'page_obj': page_obj,
        'title': 'Search'
    })
