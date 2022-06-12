from imghdr import what
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        what_is_İt = text_data_json['what_is_İt']
        user=self.scope["user"]
        print(user)
        await self.save_database(message,user,self.room_name,what_is_İt)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                "user":user.username,
                "created_date":self.message_object.get_Short_date(),
                "what_is_İt":what_is_İt
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        created_date = event['created_date']
        what_is_İt = event['what_is_İt']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            "user":user,
            "created_date":created_date,
            "what_is_İt":what_is_İt
        }))

    @database_sync_to_async
    def save_database(self,message,user,room,what_is_İt):
        m=Message.objects.create(content=message,user=user,room_id=room, what_is_İt=what_is_İt)
        self.message_object=m