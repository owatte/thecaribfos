# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thecalendar', '0008_auto_20150718_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lastupdate_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 18, 48, 8, 427403, tzinfo=utc), verbose_name='Last modification', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created on'),
        ),
    ]
