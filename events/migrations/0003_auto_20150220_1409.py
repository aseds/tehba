# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150217_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=550),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(max_length=1000, null=True, upload_to=b'images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 20, 14, 9, 56, 308000), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
