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
# configure o .gitignore
git add .
git commit -m 'Mudei o README.md's
git push
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