# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footballResults', '0005_auto_20141222_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_team_scored', models.IntegerField()),
                ('guest_team_scored', models.IntegerField()),
                ('guest_team', models.ForeignKey(related_name='guest_team', to='footballResults.FootballTeam')),
                ('home_team', models.ForeignKey(related_name='home_team', to='footballResults.FootballTeam')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='code',
            name='user_defined_code',
        ),
        migrations.RemoveField(
            model_name='document',
            name='code',
        ),
        migrations.DeleteModel(
            name='Code',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.RemoveField(
            model_name='userdefinedcode',
            name='owner',
        ),
        migrations.DeleteModel(
            name='UserDefinedCode',
        ),
    ]
