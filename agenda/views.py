from django.shortcuts import render, redirect
from agenda.models import Contact
from agenda.form import ContactForm


def home(request):
    contact = Contact.objects.all()

    return render(request, 'agenda/pages/home.html', context={
        'contacts': contact
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
    print('contact', contact)
    print(contact.phone)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('agenda:home')
    else:
        form = ContactForm(instance=contact)
        # tentar fazer com que o update form ja venha preenchido

    return render(request, 'agenda/pages/update_contact.html', context={
        'form': form,
        'contact': contact
    })


def view_contact(request, id):
    contact = Contact.objects.filter(id=id)

    return render(request, 'agenda/pages/view_contact.html', context={
        'contacts': contact
    })
