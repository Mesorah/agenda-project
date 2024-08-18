from django.shortcuts import render, redirect
from agenda.models import Contact
from agenda.form import ContactForm
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    contact = Contact.objects.all().order_by('-id')
    paginator = Paginator(contact, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # testar search

    return render(request, 'agenda/pages/home.html', context={
        'contacts': contact,
        'page_obj': page_obj,
        'var_for': page_obj
    })


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agenda:home')
    else:
        form = ContactForm()

    return render(request, 'agenda/pages/add_contact.html', context={
        'form': form
    })


def remove_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()

    return redirect('agenda:home')


def update_contact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('agenda:home')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'agenda/pages/update_contact.html', context={
        'form': form,
        'contact': contact
    })


def view_contact(request, id):
    contact = Contact.objects.filter(id=id)

    return render(request, 'agenda/pages/view_contact.html', context={
        'contacts': contact
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    contact = Contact.objects.filter(
        Q(first_name__icontains=search_term)
    ).order_by('-id')

    paginator = Paginator(contact, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agenda/pages/home.html', context={
        'contacts': contact,
        'search_term': search_term,
        'var_for': contact,
        'page_obj': page_obj
    })
