# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
#import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0002_auto_20150525_1323'),
    ]
    pass
    zooperations = [
        migrations.AlterField(
            model_name='entry',
            name='tags',

            field=models.CharField(max_length=255, blank=True),
        ),
    ]
