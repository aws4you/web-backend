
from contactmanager.models import Topic, WebPage, AccessRecord, Contact
from contactmanager.serializers import TopicSerializer, WebPageSerializer, AccessRecordSerializer, ContactSerializer

from rest_framework import viewsets, permissions

class TopicViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WebPageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = WebPage.objects.all()
    serializer_class = WebPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AccessRecordViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = AccessRecord.objects.all()
    serializer_class = AccessRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ContactViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = []
