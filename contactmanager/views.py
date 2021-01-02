from rest_framework import generics

from contactmanager.models import Topic
from contactmanager.serializers import TopicSerializer


class TopicsList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
