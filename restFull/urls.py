from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from footballResults import views
from django.contrib import admin
import settings


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^match_results/$', views.MatchResultsView.as_view()),
    url(r'^football_teams/$', views.FootballTeamsView.as_view()),
    url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view()),
    url(r'^task/$', views.TaskListView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)