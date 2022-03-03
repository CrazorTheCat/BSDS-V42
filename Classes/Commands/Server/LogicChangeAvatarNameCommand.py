from Classes.Commands.LogicServerCommand import LogicServerCommand


class LogicChangeAvatarNameCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        self.writeString(fields["Name"])
        self.writeVInt(0)
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        fields["Name"] = calling_instance.readString()
        fields["Unk1"] = calling_instance.readVInt()
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 201