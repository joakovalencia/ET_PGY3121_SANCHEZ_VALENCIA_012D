# Generated by Django 4.2.1 on 2023-07-05 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, max_length=200, verbose_name='Descripcion'),
        ),
    ]