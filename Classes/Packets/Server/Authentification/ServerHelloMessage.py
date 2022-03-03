from Classes.Packets.PiranhaMessage import PiranhaMessage


class ServerHelloMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeInt(24)
        for i in range(24):
            self.writeByte(i)

    def decode(self):
        fields = {}
        fields["Random"] = self.readBytesWithoutLength()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20100

    def getMessageVersion(self):
        return self.messageVersion