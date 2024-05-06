import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
from .serializers import *


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("message_group", self.channel_name)
        await self.send_messages()

    async def send_messages(self):
        messages = await self.messages()
        await self.send(text_data=json.dumps(messages))

    @sync_to_async
    def messages(self):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return serializer.data

    async def add_message(self, event):
        await self.send_messages()

    async def disconnect(self, code):
        await self.close()
