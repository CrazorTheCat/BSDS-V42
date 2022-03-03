from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class ChangeAvatarNameMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeString(fields["Name"])
        self.writeBoolean(fields["NameSetByUser"])

    def decode(self):
        fields = {}
        fields["Name"] = self.readString()
        fields["NameSetByUser"] = self.readBoolean()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 201}
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)
        playerData["Name"] = fields["Name"]
        playerData["Registered"] = True
        db_instance.updatePlayerData(playerData, calling_instance)
        Messaging.sendMessage(24111, fields)

    def getMessageType(self):
        return 10212

    def getMessageVersion(self):
        return self.messageVersion