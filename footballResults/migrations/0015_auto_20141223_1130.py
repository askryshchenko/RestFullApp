# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0014_auto_20141223_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballteam',
            name='img',
            field=models.ImageField(default=b'img/epl.jpg', upload_to=b'img'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 23, 11, 30, 35, 394985)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 23, 11, 30, 35, 395415)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 23, 11, 30, 35, 395400)),
            preserve_default=True,
        ),
    ]
