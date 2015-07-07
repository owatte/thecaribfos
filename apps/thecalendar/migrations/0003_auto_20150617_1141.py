# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thecalendar', '0002_event_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='email',
            field=models.EmailField(default=b'2015-06-17 15:40:51.699060+00:00@ggg.com', help_text='Email are not published on the website.', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='web',
            field=models.URLField(default=1, max_length=250, verbose_name='Web'),
            preserve_default=False,
        ),
    ]
