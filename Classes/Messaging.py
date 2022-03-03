import traceback

from Classes.ByteStream import ByteStream


class Messaging:
    def writeHeader(message, payloadLen):
        message.messageBuffer += message.getMessageType().to_bytes(2, 'big', signed=True)
        message.messageBuffer += payloadLen.to_bytes(3, 'big', signed=True)
        message.messageBuffer += message.messageVersion.to_bytes(2, 'big', signed=True)

    def readHeader(headerBytes):
        headerData = []
        headerData.append(int.from_bytes(headerBytes[:2], 'big', signed=True))
        headerData.append(int.from_bytes(headerBytes[2:5], 'big', signed=True))
        return headerData

    def sendMessage(messageType, fields, player=None):
        from Classes.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
        message = LogicLaserMessageFactory.createMessageByType(messageType, b'')
        if player is not None:
            message.encode(fields, player)
        else:
            message.encode(fields)
        Messaging.writeHeader(message, len(message.messagePayload))
        message.messageBuffer += message.messagePayload
        try:
            fields["Socket"].send(message.messageBuffer)
        except Exception:
            print(traceback.format_exc())