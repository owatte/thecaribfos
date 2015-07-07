# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0009_entry_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='email',
            field=models.EmailField(default=b'2015-06-16 20:04:43.124093+00:00@gmail.com', help_text='Email are not published on the website', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tag(s)'),
        ),
    ]
