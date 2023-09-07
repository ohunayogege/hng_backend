from django.urls import re_path as url
from .views import slackFirstTask


urlpatterns = [
    url(r'api', slackFirstTask.as_view()),
]
