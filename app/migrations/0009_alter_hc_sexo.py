# Generated by Django 4.1.3 on 2022-12-06 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_hc_alter_tv_hc_delete_historiaclinica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hc',
            name='sexo',
            field=models.IntegerField(choices=[[0, 'M'], [1, 'F']]),
        ),
    ]
