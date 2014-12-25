# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0008_auto_20141222_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 18, 37, 54, 712339)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
