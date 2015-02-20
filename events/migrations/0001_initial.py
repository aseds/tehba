# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=550)),
                ('size', models.IntegerField(default=4, max_length=6, choices=[(1, b'small'), (2, b'half'), (3, b'wide'), (4, b'square')])),
                ('image', models.ImageField(max_length=1000, null=True, upload_to=b'images/')),
                ('order', models.IntegerField(default=-10)),
                ('expired', models.BooleanField(default=False)),
                ('on', models.BooleanField(default=False)),
                ('expiration_date', models.DateTimeField(verbose_name=b'expires on')),
                ('publish_date', models.DateTimeField(default=datetime.datetime(2015, 2, 17, 17, 59, 18, 685000), verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
