from Classes.Packets.PiranhaMessage import PiranhaMessage


class OutOfSyncMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeVInt(fields["ServerChecksum"])
        self.writeVInt(fields["ClientChecksum"])
        self.writeVInt(fields["Tick"])

    def decode(self):
        fields = {}
        fields["ServerChecksum"] = self.readVInt()
        fields["ClientChecksum"] = self.readVInt()
        fields["Tick"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24104

    def getMessageVersion(self):
        return self.messageVersion