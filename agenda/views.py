from django.shortcuts import render, redirect
from agenda.models import Contact
from agenda.form import AddForm


def home(request):
    contact = Contact.objects.all()

    return render(request, 'agenda/pages/home.html', context={
        'contacts': contact
    })


def add_contact(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:home')
    else:
        form = AddForm()

    return render(request, 'agenda/pages/add_contact.html', context={
        'form': form
    })

### Terminar de testar o add_contact ###


def remove_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()

    return redirect('agenda:home')


def view_contact(request, id):
    contact = Contact.objects.filter(id=id)

    return render(request, 'agenda/pages/view_contact.html', context={
        'contacts': contact
    })
