# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('thedirectory', '0007_remove_entry_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text="Keywords (don't start keywords with a #)", verbose_name='Keyword(s)'),
        ),
    ]
