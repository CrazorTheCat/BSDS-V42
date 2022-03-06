from Classes.Wrappers.PlayerDisplayData import PlayerDisplayData

class BattleLogPlayerEntry:
    def encode(calling_instance, fields):
        pass

    def decode(calling_instance, fields):
        fields["BattleLogEntry"] = {}
        fields["BattleLogEntry"]["Unkown1"] = calling_instance.readVInt()
        fields["BattleLogEntry"]["Unkown2"] = calling_instance.readLong()
        fields["BattleLogEntry"]["Unkown3"] = calling_instance.readVInt()
        fields["BattleLogEntry"]["Unkown4"] = calling_instance.readBoolean()
        countVal = calling_instance.readVInt()
        fields["BattleLogEntry"]["Unkown5"] = countVal
        fields["BattleLogEntry"]["Entries"] = {}
        for i in range(countVal):
            fields["BattleLogEntry"]["Entries"][str(i)] = {}
            fields["BattleLogEntry"]["Entries"][str(i)]["Unknown1"] = calling_instance.readDataReference()
            fields["BattleLogEntry"]["Entries"][str(i)]["Unknown2"] = calling_instance.readVInt()
            fields["BattleLogEntry"]["Entries"][str(i)]["Unknown3"] = calling_instance.readVInt()
            fields["BattleLogEntry"]["Entries"][str(i)]["Unknown4"] = calling_instance.readVInt()
        fields["BattleLogEntry"]["Unkown6"] = calling_instance.readVInt()
        PlayerDisplayData.decode(calling_instance, fields)