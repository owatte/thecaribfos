# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thecarib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, verbose_name='Name')),
                ('slug', models.SlugField(max_length=25, verbose_name='Slug')),
                ('description', models.TextField(max_length=250, verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, verbose_name='Name')),
                ('slug', models.SlugField(max_length=25, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('web', models.URLField(max_length=250, verbose_name='Web')),
                ('lat', models.FloatField(null=True, verbose_name='Latitude')),
                ('lon', models.FloatField(null=True, verbose_name='Longitude')),
                ('twitter', models.CharField(max_length=75, null=True, verbose_name='Twitter account', blank=True)),
                ('facebook', models.CharField(max_length=75, null=True, verbose_name='Facebook page', blank=True)),
                ('googleplus', models.CharField(max_length=75, null=True, verbose_name='Google plus page', blank=True)),
                ('linkedin', models.CharField(max_length=75, null=True, verbose_name='LinkedIn page', blank=True)),
                ('category', models.ForeignKey(to='thedirectory.Category')),
                ('country', models.ForeignKey(to='thecarib.Country')),
            ],
            options={
                'ordering': ['name', 'country'],
            },
        ),
    ]
