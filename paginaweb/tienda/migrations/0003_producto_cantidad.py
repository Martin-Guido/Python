# Generated by Django 4.1 on 2022-11-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_rename_producto_producto_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
