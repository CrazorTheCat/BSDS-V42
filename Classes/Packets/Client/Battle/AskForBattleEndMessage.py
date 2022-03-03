from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class AskForBattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Unk1"] = self.readVInt()
        fields["Result"] = self.readVInt()
        fields["Rank"] = self.readVInt()
        fields["MapID"] = self.readDataReference()
        fields["HeroesCount"] = self.readVInt()
        fields["Heroes"] = []
        for i in range(fields["HeroesCount"]): fields["Heroes"].append({"Brawler": {"ID": self.readDataReference(), "SkinID": self.readDataReference()}, "Team": self.readVInt(), "IsPlayer": self.readBoolean(), "PlayerName": self.readString()})
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(23456, fields, calling_instance.player)

    def getMessageType(self):
        return 14110

    def getMessageVersion(self):
        return self.messageVersion
