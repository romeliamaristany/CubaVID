# Generated by Django 4.1.3 on 2022-12-05 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hc',
            name='CI',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='hc',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tv',
            name='lote1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tv',
            name='lote2',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tv',
            name='lote3',
            field=models.CharField(max_length=10),
        ),
    ]