# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='category',
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.CharField(default=datetime.datetime(2015, 5, 25, 17, 23, 6, 515140, tzinfo=utc), max_length=b'105'),
            preserve_default=False,
        ),
    ]
