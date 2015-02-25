# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150220_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='expired',
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 25, 6, 36, 59, 47442), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
