from rest_framework import generics

from contactmanager.models import Topic, WebPage, AccessRecord
from contactmanager.serializers import TopicSerializer, WebPageSerializer, AccessRecordSerializer


class TopicsList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class WebPagesList(generics.ListCreateAPIView):
    queryset = WebPage.objects.all()
    serializer_class = WebPageSerializer


class WebPageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WebPage.objects.all()
    serializer_class = WebPageSerializer


class AccessRecordsList(generics.ListCreateAPIView):
    queryset = AccessRecord.objects.all()
    serializer_class = AccessRecordSerializer


class AccessRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessRecord.objects.all()
    serializer_class = AccessRecordSerializer

