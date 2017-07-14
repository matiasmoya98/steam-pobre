# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0008_genero_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'static/images/genero', blank=True),
        ),
        migrations.AlterField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'static/images/juego', blank=True),
        ),
    ]
