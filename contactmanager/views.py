from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from contactmanager.models import Topic
from contactmanager.serializers import TopicSerializer


def index(request):

    vars = {
        "insert_me": "hello!"
    }

    return render(request, "index.html", context=vars)

def help(request):
    return render(request, "help.html")

class TopicsList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    # def get_object(self):
    #     pk = self.kwargs['pk']
    #     pj = Topic.objects.filter(id=pk)[0]
    #
    #     return self.serializer_class.Meta.model.objects.get(id=pk)
