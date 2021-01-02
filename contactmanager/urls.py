from django.conf.urls import url
from contactmanager.views import TopicsList

urlpatterns = [
    url(r'topic/list/$', TopicsList.as_view()),
    #url(r'topic/detail/(?P<pk>[0-9]+)/$', TopicDetail.as_view()),
]
