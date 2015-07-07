# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thecalendar', '0003_auto_20150617_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='categories',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='lat',
            field=models.FloatField(null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='event',
            name='lon',
            field=models.FloatField(null=True, verbose_name='Longitude'),
        ),
    ]
