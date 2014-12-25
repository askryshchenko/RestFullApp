from footballResults.models import *
from rest_framework import serializers
from datetime import datetime


class FootballTeamSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        if data['country'] == "Russia":
            raise serializers.ValidationError("In Russia no football")

        return data

    class Meta:
        model = FootballTeam
        fields = ('name', 'country', 'city')


class MatchResultSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['home_team_scored'] < 0 or data['guest_team_scored'] < 0:
            raise serializers.ValidationError("Uncorrect scored value")
        if data['date'] > datetime.date(datetime.now()):
            raise serializers.ValidationError("You don't know a future")
        if data['home_team'] == data['guest_team']:
            raise serializers.ValidationError("It's impossible to play with yourself")
        return data

    class Meta:
        model = MatchResult
        fields = ('home_team', 'guest_team', 'home_team_scored', 'guest_team_scored', 'date')
        depth = 1


class TaskSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if 'task_id' not in data or 'team' not in data or 'start_date' not in data \
                or 'end_date' not in data or data['task_id'] < 0:
            raise serializers.ValidationError("Uncorrect format data")
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must occur after start date")

        get_team_by_name(data['team'])
        return data


    class Meta:
        model = Task
        fields = ('task_id', 'team', 'start_date', 'end_date')
        depth = 1
