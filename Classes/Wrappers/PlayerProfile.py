from Classes.Logic.LogicLong import LogicLong
from Classes.Wrappers.PlayerDisplayData import PlayerDisplayData

class PlayerProfile:
    def encode(calling_instance, fields, playerData):
        calling_instance.encodeLogicLong(LogicLong(fields["PlayerID"][0], fields["PlayerID"][1]))
        calling_instance.writeDataReference(0)

        sortedBrawlers = sorted(playerData["OwnedBrawlers"], key=lambda x: (playerData["OwnedBrawlers"][x]['Trophies']), reverse=True)

        calling_instance.writeVInt(len(sortedBrawlers))
        for brawlerID in sortedBrawlers:
            brawlerData = playerData["OwnedBrawlers"][brawlerID]
            calling_instance.writeDataReference(16, brawlerID)
            if brawlerData["Skins"] != []:
                calling_instance.writeDataReference(29, brawlerData["Skins"][0]) # TODO: Sync with current skin
            else:
                calling_instance.writeDataReference(0)
            calling_instance.writeVInt(brawlerData["Trophies"])
            calling_instance.writeVInt(brawlerData["HighestTrophies"])
            calling_instance.writeVInt(brawlerData["PowerLevel"])

        calling_instance.writeVInt(16)

        calling_instance.writeVInt(1)
        calling_instance.writeVInt(9999)        
        
        calling_instance.writeVInt(2)
        calling_instance.writeVInt(playerData["Experience"])

        calling_instance.writeVInt(3)
        calling_instance.writeVInt(playerData["Trophies"])

        calling_instance.writeVInt(4)
        calling_instance.writeVInt(playerData["HighestTrophies"])

        calling_instance.writeVInt(5)
        calling_instance.writeVInt(len(sortedBrawlers))

        calling_instance.writeVInt(8)
        calling_instance.writeVInt(9999)

        calling_instance.writeVInt(11)
        calling_instance.writeVInt(9999)

        calling_instance.writeVInt(9)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(12)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(13)
        calling_instance.writeVInt(100)

        calling_instance.writeVInt(14)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(15)
        calling_instance.writeVInt(9999)

        calling_instance.writeVInt(16)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(18)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(17)
        calling_instance.writeVInt(0)

        calling_instance.writeVInt(19)
        calling_instance.writeVInt(0)

        PlayerDisplayData.encode(calling_instance, playerData)

    def decode(calling_instance, fields):
        pass