# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0008_entry_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(default=1, to='thedirectory.Category'),
            preserve_default=False,
        ),
    ]
