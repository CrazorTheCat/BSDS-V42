import Configuration
from Classes.ByteStream import ByteStream
from Classes.Utility import Utility


class PiranhaMessage(ByteStream):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageBuffer = messageData
        self.fields = {}

    def decode(self, fields):
        if Configuration.settings['PrintEnabled']:
            Utility.parseFields(fields)

    def getLength(self):
        return len(self.messageBuffer)

    def isServerToClient(self):
        messageType = self.getMessageType()
        if 20000 <= messageType < 30000 or messageType == 40000:
            return True
        elif 10000 <= messageType < 20000 or messageType == 30000:
            return False
