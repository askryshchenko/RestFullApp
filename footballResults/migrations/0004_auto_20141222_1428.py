# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0003_remove_matchresult_guest_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_team_scored', models.IntegerField()),
                ('guest_team_scored', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='matchresult',
            name='home_team',
        ),
        migrations.DeleteModel(
            name='MatchResult',
        ),
    ]
