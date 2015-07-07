# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thecarib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='iso',
            field=models.SlugField(help_text='iso 3166 code', unique=True, max_length=b'5', verbose_name='Iso code'),
        ),
    ]
