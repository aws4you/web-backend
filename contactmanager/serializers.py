from rest_framework import serializers

from contactmanager.models import Topic, WebPage, AccessRecord


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class WebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebPage
        fields = '__all__'


class AccessRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRecord
        fields = '__all__'

