from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer, XMLRenderer, JSONRenderer
from footballResults.serializers import *
from rest_framework import renderers


class PlainTextRenderer(renderers.BaseRenderer):
    """
    Renderer for text format
    """
    media_type = 'plain/text'
    format = 'text'

    def render(self, data, media_type=None, renderer_context=None):
        return str(data)


class IndexView(APIView):
    """
    Main page view
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, XMLRenderer, PlainTextRenderer)
    template_name = "index.html"

    def get(self, request, format=None):
        return Response({})


class FootballTeamsView(APIView):
    """
    GET all football teams
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, XMLRenderer, PlainTextRenderer)
    template_name = "football_teams.html"

    def get(self, request, format=None):
        queryset = FootballTeam.objects.all()
        content = {'queryset': queryset}
        return Response(content)


class MatchResultsView(APIView):
    """
    GET all match results
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, XMLRenderer, PlainTextRenderer)
    template_name = "match_results.html"

    def get(self, request, format=None):
        queryset = MatchResult.objects.all()
        serializer = MatchResultSerializer(queryset, many=True)
        content = {'queryset': serializer.data}
        return Response(content)


class TaskListView(APIView):
    """
    List all Tasks, or create a new task.
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, XMLRenderer, PlainTextRenderer)
    template_name = "task_list.html"

    def get(self, request, format=None):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        content = {'queryset': serializer.data}
        return Response(content)


    def put(this, request, format=None):

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # response_format = request.accepted_renderer.format
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    """
    GET task by task_id or POST change into task or DELETE task
    """
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, XMLRenderer, PlainTextRenderer)
    template_name = 'task.html'

    def get(self, request, pk, format=None):
        task = get_task_by_id(pk)
        team = get_team_by_name(task.team)
        queryset = get_task_data(task, team)
        serializer = MatchResultSerializer(queryset, many=True)
        response_format = request.accepted_renderer.format
        if response_format == 'html':
            content = {'match_results': serializer.data, 'task': task, 'team': team}
            return Response(content)
        content = serializer.data
        return Response(content)

    def post(self, request, pk, format=None):
        task = get_task_by_id(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = get_task_by_id(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)