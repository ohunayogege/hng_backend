from django.urls import re_path as url, path
from .views import slackFirstTask, CreatePerson


urlpatterns = [
    # url(r'api', slackFirstTask.as_view()),
    url(r'^api$', CreatePerson.as_view()),
    url(r'^api/(?P<pk>\d+)$', CreatePerson.as_view()),
]
