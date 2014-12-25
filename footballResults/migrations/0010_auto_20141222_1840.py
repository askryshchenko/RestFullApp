# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0009_auto_20141222_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 18, 40, 24, 158458)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 18, 40, 24, 158443)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 18, 40, 24, 158034)),
            preserve_default=True,
        ),
    ]
