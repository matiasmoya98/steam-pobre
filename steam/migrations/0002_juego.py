# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('fecha_de_lanzamiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('distribuidor', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
