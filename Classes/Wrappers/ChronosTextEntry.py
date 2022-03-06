from Classes.ByteStream import ByteStream

class ChronosTextEntry:
    @staticmethod
    def decode(byteStream: ByteStream):
        fields = []
        fields.append(byteStream.readInt())
        fields.append(byteStream.readStringReference())
        return fields
        