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
