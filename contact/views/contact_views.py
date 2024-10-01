from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q
from contact.models import Contact


def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[0:10]

    print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()
    # print('search_value', search_value) # query dict
    if search_value == '':
        # redireciona para o index quando o valor pesquisado é vazio
        return redirect('contact:index')

    print(search_value)

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')
    
    print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()

    # if single_contact is None:
    #     raise Http404()

    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )