from django.conf.urls import url, include
from contactmanager.views import index, help, TopicsList

urlpatterns = [
    url(r'^$', index),
    url(r'^help/', help),

    url(r'topic/list/$', TopicsList.as_view()),
    #url(r'topic/detail/(?P<pk>[0-9]+)/$', TopicDetail.as_view()),

]
