## Iniciar o projeto Django
```
python -m venv venv
. venv/bin/activate 1
pip install django
django-admin startproject project
python manage.py startapp contact
- adicionar no settings.py:
    Em TEMPLATES:
        'DIRS': [
            BASE_DIR / 'base_templates'],

    STATICFILES_DIRS = (
        BASE_DIR / 'base_static',
    )
```

## Configurar o git
```
git config --global user.name 'Seu Nome'
git config --global user.email 'Seu email'
git config --global init.defaultBranch main
### configure o .gitignore
- git init
- git add .
- git commit -m 'Mensagem'
- git log -> exibe dados sobre os commits
- git remote add origin URL_DO_GIT
- git add .
- git commit -m 'mudei'
- git push origin main -u
    -> origin -> nome da origin
    -> main -> nome da main
- git push
```

## migrando a base de dados do Django
```
python manage.py makemigrations
python manage.py migrate
```

## Criando e modificando a senha de um super usuário Django
```
python manage.py createsuperuser

-> em caso de esquecer a sua senha: 
python manage.py changepassword USERNAME
```
obs: passwordsgenerator.net -> gerador de senhas fortes
- Links úteis:
    - https://docs.djangoproject.com/en/5.1/topics/db/models/
    - https://docs.djangoproject.com/en/5.1/ref/models/fields/

## aula 453 - django models
- Nesta aula vamos criar a classe Contact em models.py de contact
- toda vez que editarmos o nosso model devemos executar os seguintes comando:
```
python manage.py makemigrations
python manage.py migrate
```

## aula 455 - Customizando as opçoes admin.ModelAdmin
- NOTA: quando for trabalhar com tuplas sem o uso de parenteses, semmpre coloque uma vírgula(,) ao final.
- é bom tomar cuidado com a mostra da lista de itens porque se voce tiver muitos itens a se exibido, provocará um hit grande na base de dados

Código:
~~~python
# contacct/admin.py
from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name'
~~~

## aula 457 - Criando um ImageField e configurando MEDIA_URL e MEDIA_ROOT no settings.py

```python
# Importe o módulo
from contact.models import Contact
# Cria um contato(Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Seleciona um contato com id 10
# retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo Valor 2'
contact.save()
# apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valorea manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenados por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order('-id')
```


## aula 471 - Filtrando valores com Q e OR para o campo de pesquisa

~~~python
from django.db.models import Q

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
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )
~~~
