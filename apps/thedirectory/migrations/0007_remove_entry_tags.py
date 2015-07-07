# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0006_auto_20150602_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='tags',
        ),
    ]
