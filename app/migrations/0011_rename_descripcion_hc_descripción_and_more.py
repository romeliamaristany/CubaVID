# Generated by Django 4.1.3 on 2022-12-10 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_tv_hc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hc',
            old_name='descripcion',
            new_name='descripción',
        ),
        migrations.RenameField(
            model_name='hc',
            old_name='direccion',
            new_name='dirección',
        ),
        migrations.RenameField(
            model_name='hc',
            old_name='telefono',
            new_name='teléfono',
        ),
    ]
