from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.PlayerProfile import PlayerProfile
from Database.DatabaseHandler import DatabaseHandler

class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(fields["PlayerID"])
        PlayerProfile.encode(self, fields, playerData)
        self.writeBoolean(False) # TODO: Club
        self.writeDataReference(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion