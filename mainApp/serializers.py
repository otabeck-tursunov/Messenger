from rest_framework.serializers import ModelSerializer

from .models import Message, Chat


class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class ChatAccountSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessagePostSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'chat', 'message')
