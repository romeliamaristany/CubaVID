# Generated by Django 4.1.3 on 2022-12-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_tv_fecha_primera_dosis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv',
            name='enfermera_primera_dosis',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tv',
            name='enfermera_segunda_dosis',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tv',
            name='enfermera_tercera_dosis',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tv',
            name='fecha_primera_dosis',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='tv',
            name='fecha_segunda_dosis',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='tv',
            name='fecha_tercera_dosis',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='tv',
            name='hora_primera_dosis',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tv',
            name='hora_segunda_dosis',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tv',
            name='hora_tercera_dosis',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tv',
            name='lote_primera_dosis',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='tv',
            name='lote_segunda_dosis',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='tv',
            name='lote_tercera_dosis',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]