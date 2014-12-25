# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0002_remove_matchresult_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchresult',
            name='guest_team',
        ),
    ]
