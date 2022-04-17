from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class AvatarNameCheckResponseMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString(fields["Name"])

    def decode(self):
        fields = {}
        fields["Unk1"] = self.readBoolean()
        fields["Unk2"] = self.readInt()
        fields["Name"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20300

    def getMessageVersion(self):
        return self.messageVersion
