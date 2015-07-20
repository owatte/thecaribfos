# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0013_auto_20150617_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.TextField(help_text='Use Markdown to format you description text', verbose_name='Description'),
        ),
    ]
