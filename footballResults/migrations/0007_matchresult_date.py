# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0006_auto_20141222_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 22, 14, 44, 5, 721646)),
            preserve_default=True,
        ),
    ]
