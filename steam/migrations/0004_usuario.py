# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0003_auto_20170616_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
                ('descripcion_user', models.TextField()),
                ('nacionalidad', models.CharField(max_length=200)),
            ],
        ),
    ]
