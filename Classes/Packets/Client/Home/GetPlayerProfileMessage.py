from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.BattleLogPlayerEntry import BattleLogPlayerEntry


class GetPlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["PlayerID"] = self.readLong()
        boolVal = self.readBoolean()
        fields["isBattleLog"] = boolVal
        if boolVal:
            BattleLogPlayerEntry.decode(self, fields)
        fields["Unknown"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24113, fields)

    def getMessageType(self):
        return 14113

    def getMessageVersion(self):
        return self.messageVersion