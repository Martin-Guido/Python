# Generated by Django 4.1 on 2022-11-06 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='producto',
            new_name='nombre',
        ),
    ]
