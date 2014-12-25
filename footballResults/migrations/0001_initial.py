# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MatchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_team_scored', models.IntegerField()),
                ('guest_team_scored', models.IntegerField()),
                ('date', models.DateField()),
                ('guest_team', models.ForeignKey(related_name='GuestTeam', to='footballResults.FootballTeam')),
                ('home_team', models.ForeignKey(related_name='HomeTeam', to='footballResults.FootballTeam')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
