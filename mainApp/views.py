from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class MessagesAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessagePostSerializer(data=request.data)
        if serializer.is_valid():
            accounts = ChatAccount.objects.filter(
                chat=serializer.validated_data['chat']
            ).values_list('account__username', flat=True)
            print(accounts)
            if request.user.username not in accounts:
                return Response({"success": False, "message": "Chatda user mavjud emas!"}, status=HTTP_400_BAD_REQUEST)
            serializer.save(account=request.user)

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'message_group',
                {
                    "type": "add_message",
                }
            )
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)
