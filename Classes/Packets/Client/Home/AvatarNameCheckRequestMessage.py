from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class AvatarNameCheckRequestMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Name"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(20300, fields)

    def getMessageType(self):
        return 14600

    def getMessageVersion(self):
        return self.messageVersion