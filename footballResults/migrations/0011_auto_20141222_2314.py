# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0010_auto_20141222_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 14, 44, 329160)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 14, 44, 329713)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 14, 44, 329693)),
            preserve_default=True,
        ),
    ]
