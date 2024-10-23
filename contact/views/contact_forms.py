from django.shortcuts import render, redirect

from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            # commit = False > não salva diretamente no banco de dados
            # contact = form.save(commit=False)
            # contact.show = True
            # contact.save()
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context
        )


    context = {
        'form': ContactForm()
    }


    return render(
        request,
        'contact/create.html',
        context
    )