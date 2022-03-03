from Classes.Packets.PiranhaMessage import PiranhaMessage


class KeepAliveServerMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20108

    def getMessageVersion(self):
        return self.messageVersion