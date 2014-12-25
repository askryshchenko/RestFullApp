from django.db import models
from datetime import datetime
from django.db.models import Q
from django.http import Http404

class FootballTeam(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img', default='img/epl.jpg')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return "name: " + self.name + "from "  + self.city + self.country

def get_team_by_name(team_name):
        try:
            return FootballTeam.objects.get(name=team_name)
        except FootballTeam.DoesNotExist:
            raise Http404



class MatchResult(models.Model):
    home_team = models.ForeignKey(to=FootballTeam, related_name="home_team")
    guest_team = models.ForeignKey(to=FootballTeam, related_name="guest_team")
    home_team_scored = models.IntegerField()
    guest_team_scored = models.IntegerField()
    date = models.DateField(default=datetime.now())

    def __str__(self):
        return "Home team: " + str(self.home_team) + " - " + "Guest Team: " + str(self.guest_team) + str(self.home_team_scored) + ":" + str(self.guest_team_scored) + " date: " + str(self.date)

def get_match_result(pk):
        try:
            return MatchResult.objects.get(pk=pk)
        except MatchResult.DoesNotExist:
            raise Http404


class Task(models.Model):
    task_id = models.IntegerField(unique=True, default=0)
    team = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(default=datetime.now())


def get_task_data(task, team):
        home_query = MatchResult.objects.filter(date__gte=task.start_date
        ).filter(date__lte=task.end_date
        ).filter(Q(home_team=team.pk) | Q(guest_team=team.pk))

        return home_query


def get_task_by_id(pk):
        try:
            return Task.objects.get(task_id=pk)
        except Task.DoesNotExist:
            raise Http404
