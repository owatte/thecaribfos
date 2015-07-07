# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, verbose_name='Name')),
                ('iso', models.SlugField(unique=True, max_length=b'2', verbose_name='Iso code')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
