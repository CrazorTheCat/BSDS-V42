from io import BytesIO

from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class BattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeLong(0, 1)
        self.writeLong(0, 1)
        self.writeVInt(1) # Battle End Game Mode
        self.writeVInt(fields["Rank"]) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVInt(0) # Tokens Gained
        self.writeVInt(1250) # Trophies Result
        self.writeVInt(0) # Power Play Points Gained
        self.writeVInt(0) # Doubled Tokens
        self.writeVInt(0) # Double Token Event
        self.writeVInt(0) # Token Doubler Remaining
        self.writeVInt(0) # Special Events Level Passed
        self.writeVInt(0) # Epic Win Power Play Points Gained
        self.writeVInt(0) # Championship Level Reached
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(True)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)

        self.writeVInt(fields["HeroesCount"])
        for heroEntry in fields["Heroes"]:
            self.writeBoolean(heroEntry["IsPlayer"])
            self.writeBoolean(bool(heroEntry["Team"]))
            self.writeBoolean(bool(heroEntry["Team"]))
            self.writeVInt(1)
            for i in range(1):
                self.writeDataReference(heroEntry["Brawler"]["ID"][0], heroEntry["Brawler"]["ID"][1])
            self.writeVInt(1)
            for i in range(1):
                self.writeDataReference(heroEntry["Brawler"]["SkinID"][0], heroEntry["Brawler"]["SkinID"][1])
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1250)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(11)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(heroEntry["IsPlayer"])
            if heroEntry["IsPlayer"]:
                self.writeLong(player.ID[0], player.ID[1])
            self.writeString(heroEntry["PlayerName"])
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)
            self.writeVInt(46000000)
            if heroEntry["IsPlayer"]:
                self.writeBoolean(True)
                self.writeVLong(5, 4181497)
                self.writeString('Orange eSPORT')
                self.writeDataReference(8, 16)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(2)

        self.writeVInt(1)
        self.writeVInt(1250)
        self.writeVInt(1250)

        self.writeVInt(5)
        self.writeVInt(999999)
        self.writeVInt(999999)

        self.writeDataReference(28, 0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)

    def decode(self):
        fields = {}
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23456

    def getMessageVersion(self):
        return self.messageVersion