# Generated by Django 5.2 on 2025-05-06 20:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistas_quillayquen', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cotizacion',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='telefono',
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
