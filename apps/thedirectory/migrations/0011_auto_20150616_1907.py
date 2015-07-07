# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thedirectory', '0010_auto_20150616_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='address',
            field=models.TextField(null=True, verbose_name='Address', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='email',
            field=models.EmailField(help_text='Email are not published on the website.', max_length=254, verbose_name='Email'),
        ),
    ]
