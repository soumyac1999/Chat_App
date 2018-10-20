from django.urls import path, include
from . import consumer

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', consumer.ChatConsumer)
]
