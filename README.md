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

```

## migrando a base de dados do Django

