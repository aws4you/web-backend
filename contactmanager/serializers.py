from rest_framework import serializers

from contactmanager.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    #top_name = serializers.CharField(max_length=32)

    class Meta:
        model = Topic
        fields = '__all__'
