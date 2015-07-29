# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0016_auto_20150728_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='sequence',
            field=models.SmallIntegerField(default=0, verbose_name='Update number'),
        ),
    ]
