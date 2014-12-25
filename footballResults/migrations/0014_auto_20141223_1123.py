# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0013_auto_20141222_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballteam',
            name='img',
            field=models.ImageField(default=b'static/img/epl.jpg', upload_to=b'media'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 23, 11, 23, 38, 117333)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 23, 11, 23, 38, 117782)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 23, 11, 23, 38, 117766)),
            preserve_default=True,
        ),
    ]
