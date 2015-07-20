# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thecalendar', '0006_auto_20150617_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='Use Markdown to format you description text', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sequence',
            field=models.SmallIntegerField(default=0, verbose_name='Update number'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(default=b'pending', max_length=10, verbose_name='Status', choices=[(b'tentative', 'tentative'), (b'confirmed', 'confirmed'), (b'cancelled', 'cancelled')]),
        ),
    ]
