import uuid
from datetime import datetime

MESSAGES_DB = []

class Message:
    def __init__(self, id, content, sender, timestamp=None):
        self.id = id
        self.content = content
        self.sender = sender
        self.timestamp = timestamp or datetime.now()
    
    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "sender": self.sender,
            "timestamp": self.timestamp.isoformat()
        }
