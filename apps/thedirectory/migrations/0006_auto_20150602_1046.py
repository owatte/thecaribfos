# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0005_auto_20150602_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
