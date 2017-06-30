# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0005_auto_20170630_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(null=True, upload_to='static/images', blank=True),
        ),
    ]
