# Generated by Django 4.1.3 on 2022-12-06 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_tv_enfermera_primera_dosis_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HC',
            new_name='HistoriaClinica',
        ),
    ]