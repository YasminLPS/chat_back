from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MESSAGES_DB, Message
from .serializers import MessageSerializer
from uuid import uuid4
from datetime import datetime

class MessageListCreateAPIView(APIView):
    def get(self, request):
        # Ordenar mensagens por timestamp
        messages = sorted(MESSAGES_DB, key=lambda x: x.timestamp)
        serialized = [msg.to_dict() for msg in messages]
        return Response(serialized, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        data['id'] = data.get('id', str(uuid4()))  # Gera UUID se não for fornecido
        data['timestamp'] = data.get('timestamp', datetime.utcnow())
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            message = Message(**serializer.validated_data)
            MESSAGES_DB.append(message)
            return Response(message.to_dict(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
