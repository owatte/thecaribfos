# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0011_auto_20150616_1907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['name', 'country'], 'verbose_name_plural': 'Entries'},
        ),
    ]
