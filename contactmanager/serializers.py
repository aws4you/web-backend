from rest_framework import serializers

from contactmanager.models import Topic, WebPage, AccessRecord, Contact


class TopicSerializer(serializers.ModelSerializer):

    # Before creating this field we should define foreign key with parameter related_name='webpages'
    # in the WebPage model
    webpages = serializers.HyperlinkedRelatedField(many=True, view_name='webpage-detail', read_only=True)

    class Meta:
        model = Topic
        fields = ['url', 'id', 'top_name', 'webpages']


class WebPageSerializer(serializers.ModelSerializer):

    topic = serializers.HyperlinkedRelatedField(many=False, view_name='topic-detail', read_only=True)
    accessrecords = serializers.HyperlinkedRelatedField(many=True, view_name='accessrecord-detail', read_only=True)

    class Meta:
        model = WebPage
        fields = ['url', 'topic_id', 'name', 'topic', 'webpage_url', 'accessrecords']


class AccessRecordSerializer(serializers.ModelSerializer):

    name = serializers.HyperlinkedRelatedField(many=False, view_name='webpage-detail', read_only=True)
    page_name = serializers.ReadOnlyField(source='name.name')

    class Meta:
        model = AccessRecord
        fields = ['url', 'page_name', 'date', 'name']

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = [ 'id', 'name', 'email', 'phone' ]