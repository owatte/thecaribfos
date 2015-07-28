# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0015_entry_creation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 18, 57, 25, 658326, tzinfo=utc), verbose_name='Created on', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='lastupdate_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 18, 57, 40, 566441, tzinfo=utc), verbose_name='Last modification', auto_now=True),
            preserve_default=False,
        ),
    ]
