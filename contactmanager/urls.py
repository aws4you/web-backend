from django.conf.urls import url
from contactmanager.views import TopicsList, WebPagesList, AccessRecordsList, TopicDetail, WebPageDetail, \
    AccessRecordDetail

urlpatterns = [
    url(r'topic/list/$', TopicsList.as_view()),
    url(r'topic/detail/(?P<pk>[0-9]+)/$', TopicDetail.as_view()),

    url(r'webpage/list/$', WebPagesList.as_view()),
    url(r'webpage/detail/(?P<pk>[0-9]+)/$', WebPageDetail.as_view()),

    url(r'accessrecord/list/$', AccessRecordsList.as_view()),
    url(r'accessrecord/detail/(?P<pk>[0-9]+)/$', AccessRecordDetail.as_view()),
]
