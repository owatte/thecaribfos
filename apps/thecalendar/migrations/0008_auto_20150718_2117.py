# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thecalendar', '0007_auto_20150717_1801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='user',
            new_name='creation_user',
        ),
    ]
