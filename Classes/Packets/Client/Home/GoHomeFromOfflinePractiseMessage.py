from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class GoHomeFromOfflinePractiseMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        self.readBoolean()
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24101, fields, calling_instance.player)

    def getMessageType(self):
        return 14109

    def getMessageVersion(self):
        return self.messageVersion