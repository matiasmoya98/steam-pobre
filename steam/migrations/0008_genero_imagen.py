# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steam', '0007_auto_20170706_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'static/images', blank=True),
        ),
    ]
