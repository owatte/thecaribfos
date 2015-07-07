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
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('slug', models.SlugField(max_length=25, verbose_name='Slug')),
                ('description', models.TextField(max_length=250, verbose_name='Description')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'confirmed', max_length=10, verbose_name='Status', choices=[(b'tentative', 'tentative'), (b'confirmed', 'confirmed'), (b'cancelled', 'cancelled')])),
                ('dtstart', models.DateTimeField(verbose_name='From')),
                ('dtend', models.DateTimeField(verbose_name='To')),
                ('allday', models.BooleanField(verbose_name='All day')),
                ('summary', models.CharField(max_length=75, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('location', models.CharField(max_length=250, verbose_name='Location')),
                ('address', models.TextField(max_length=250, verbose_name='Address')),
                ('slug', models.SlugField(max_length=35, verbose_name='Slug')),
                ('sequence', models.SmallIntegerField(verbose_name='Update number')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Last modification')),
                ('pub_status', models.CharField(default=b'pending', max_length=10, verbose_name='Publication status', choices=[(b'draft', 'draft'), (b'pending', 'pending'), (b'published', 'published')])),
                ('categories', models.ManyToManyField(to='thecalendar.Category')),
                ('country', models.ForeignKey(to='thecarib.Country')),
            ],
            options={
                'ordering': ['dtstart', 'country', 'summary'],
            },
        ),
    ]
