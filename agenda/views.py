from django.shortcuts import render, redirect
from agenda.models import Contact
from agenda.form import ContactForm, CategoryForm, RemoveCategoryForm, UpdateCategoryForm # noqa E501
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages


def home(request):
    contact = Contact.objects.all().order_by('-id')
    paginator = Paginator(contact, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agenda/pages/home.html', context={
        'contacts': contact,
        'page_obj': page_obj,
        'var_for': page_obj,
        'title': 'Home'
    })


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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


def remove_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request, 'Contact successfully removed!')

    return redirect('agenda:home')


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


def update_contact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            messages.success(request, 'Contact Successfully Changed!')
            form.save()
            return redirect('agenda:home')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'agenda/pages/update_contact.html', context={
        'form': form,
        'contact': contact
    })


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


def view_contact(request, id):
    contact = Contact.objects.filter(id=id)

    return render(request, 'agenda/pages/view_contact.html', context={
        'contacts': contact
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    contact = Contact.objects.filter(
        Q(
            Q(id__icontains=search_term) |
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term) |
            Q(phone__icontains=search_term) |
            Q(email__icontains=search_term)
        )
    ).order_by('-id')

    paginator = Paginator(contact, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agenda/pages/home.html', context={
        'contacts': contact,
        'search_term': search_term,
        'var_for': contact,
        'page_obj': page_obj,
        'title': 'search'
    })
