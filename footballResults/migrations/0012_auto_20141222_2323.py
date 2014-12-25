# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0011_auto_20141222_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 23, 21, 8896)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 23, 21, 9351)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 23, 21, 9335)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='team',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
