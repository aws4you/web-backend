from django.conf.urls import url
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from contactmanager.views import TopicsList, WebPagesList, AccessRecordsList, TopicDetail, WebPageDetail, \
    AccessRecordDetail

urlpatterns = [
    url(r'topic/$', TopicsList.as_view()),
    #path('topic/', TopicsList.as_view()),
    url(r'topic/<int:pk>/$', TopicDetail.as_view()),
    #path('topic/<int:pk>/', TopicDetail.as_view()),

    url(r'webpage/$', WebPagesList.as_view()),
    url(r'webpage/(?P<pk>[0-9]+)/$', WebPageDetail.as_view()),

    url(r'accessrecord/$', AccessRecordsList.as_view()),
    url(r'accessrecord/(?P<pk>[0-9]+)/$', AccessRecordDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)