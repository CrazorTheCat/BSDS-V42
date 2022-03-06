class PlayerDisplayData:
    def encode(calling_instance, playerData):
        calling_instance.writeString(playerData["Name"])
        calling_instance.writeVInt(100)
        calling_instance.writeVInt(28000000 + playerData["Thumbnail"])
        calling_instance.writeVInt(43000000 + playerData["Namecolor"])
        calling_instance.writeVInt(0)

    def decode(calling_instance, fields):
        fields["PlayerDisplayData"] = {}
        fields["PlayerDisplayData"]["Name"] = calling_instance.readString()
        fields["PlayerDisplayData"]["Unknown"] = calling_instance.readVInt()
        fields["PlayerDisplayData"]["Thumbnail"] = calling_instance.readVInt()
        fields["PlayerDisplayData"]["Namecolor"] = calling_instance.readVInt()
        fields["PlayerDisplayData"]["Unknown"] = calling_instance.readVInt()