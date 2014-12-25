# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0012_auto_20141222_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 34, 34, 134585)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 34, 34, 135218)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 23, 34, 34, 135195)),
            preserve_default=True,
        ),
    ]
