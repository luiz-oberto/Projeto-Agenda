# Generated by Django 5.1.1 on 2024-10-30 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Telefone'),
        ),
    ]
