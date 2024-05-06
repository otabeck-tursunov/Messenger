from rest_framework.status import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class MessagesAPIView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'message_group',
                {
                    "type": "add_message",
                }
            )
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)
