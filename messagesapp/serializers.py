from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    content = serializers.CharField(max_length=500)
    sender = serializers.CharField(max_length=100)
    timestamp = serializers.DateTimeField(required=False)
