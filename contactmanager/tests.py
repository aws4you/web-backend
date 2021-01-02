from collections import OrderedDict

from django.test import TestCase, RequestFactory
from rest_framework.test import APITestCase
from contactmanager.views import TopicsList
from pprint import pprint

class ContactManagerTests(APITestCase):
    fixtures = ['topic.json', 'webpage.json', 'access-record.json']

    def setUp(self) -> None:
        self.factory = RequestFactory()

    def topics_list(self) -> OrderedDict:
        request = self.factory.get('/contactmanager/topic/list/')

        response = TopicsList.as_view()(request)

        return response.data

    def test_topic_list_count(self):
        self.assertTrue(len(self.topics_list()) == 5)
