import zlib

from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.ChecksumEncoder import ChecksumEncoder
from Classes.Logic.LogicStringUtil import LogicStringUtil
from Classes.Debugger import Debugger
from Classes.Logic.LogicLong import LogicLong


class ByteStream(ChecksumEncoder):
    def __init__(self, messageBuffer, unknown=0):
        super().__init__()
        self.messagePayload = messageBuffer
        self.bitoffset = 0
        self.offset = 0
        self.length = len(self.messagePayload)

    def clear(self, length):
        if self.messagePayload:
            self.messagePayload = b''
        self.bitoffset = 0
        self.offset = 0

    def destroy(self):
        self.messagePayload = None
        self.bitoffset = 0
        self.offset = 0
        self.length = 0

    def ensureCapacity(self, length):
        offset = self.offset
        if len(self.messagePayload) < offset + length:
            buffer_copy = self.messagePayload
            buf_len = length
            self.length = buf_len
            self.messagePayload += bytes([0] * buf_len)

    def getBitOffset(self):
        return self.bitoffset

    def getByteArray(self):
        return self.messagePayload

    def getCapacityIncrement(self):
        return 100

    def getDataPointer(self):
        return self.messagePayload[self.offset]

    def getLength(self):
        length = self.length
        if self.length <= self.offset:
            length = self.offset
        return length

    def getOffset(self):
        return self.offset

    @staticmethod
    def getVIntSizeInBytes(value):
        if value < 0:
            if value > -64:
                return 1
            elif value > -8192:
                return 2
            elif value > -1048576:
                return 3
            elif value > -134217727:
                return 4
            else:
                return 5
        else:
            if value < 64:
                return 1
            elif value < 8192:
                return 2
            elif value < 1048576:
                return 3
            elif value < 134217727:
                return 4
            else:
                return 5

    @staticmethod
    def getVLongSizeInBytes(value):
        if value < 0:
            if value > -64:
                return 1
            elif value > -8192:
                return 2
            elif value > -1048576:
                return 3
            elif value > -134217727:
                return 4
            elif value > -17179869184:
                return 5
            elif value > -2199023255552:
                return 6
            elif value > -281474976710656:
                return 7
            elif value > -36028797018963968:
                return 8
            elif value > -4611686018427387903:
                return 9
            else:
                return 10
        else:
            if value < 64:
                return 1
            elif value < 8192:
                return 2
            elif value < 1048576:
                return 3
            elif value < 134217727:
                return 4
            elif value < 17179869184:
                return 5
            elif value < 2199023255552:
                return 6
            elif value < 281474976710656:
                return 7
            elif value < 36028797018963968:
                return 8
            elif value < 4611686018427387903:
                return 9
            else:
                return 10

    def isAtEnd(self):
        return len(self.messagePayload) <= self.offset

    @staticmethod
    def isByteStream():
        return True

    @staticmethod
    def isCheckSumOnlyMode():
        return False

    def readBoolean(self):
        bitoffset = self.bitoffset
        offset = self.offset + (8 - bitoffset >> 3)
        self.offset = offset
        self.bitoffset = bitoffset + 1 & 7
        return (1 << (bitoffset & 31) & self.messagePayload[offset - 1]) != 0
    # region Read

    def readByte(self):
        self.bitoffset = 0
        result = self.messagePayload[self.offset]
        self.offset += 1
        return result

    def readBytes(self, length, max=1000):
        self.bitoffset = 0
        if (length & 0x80000000) != 0:
            if length != -1:
                Debugger.warning("Negative readBytes length encountered.")
        elif length <= max:
            result = self.messagePayload[self.offset:self.offset + length]
            self.offset += length
            return bytes(result)
        else:
            Debugger.warning("readBytes too long array, max", max)
        return b''

    def readBytesLength(self):
        self.bitoffset = 0
        result = (self.messagePayload[self.offset] << 24)
        result += (self.messagePayload[self.offset + 1] << 16)
        result += (self.messagePayload[self.offset + 2] << 8)
        result += (self.messagePayload[self.offset + 3])
        self.offset += 4
        return result

    def readInt8(self):
        self.bitoffset = 0
        result = (self.messagePayload[self.offset])
        self.offset += 1
        return result

    def readInt16(self):
        self.bitoffset = 0
        result = (self.messagePayload[self.offset] << 8)
        result += (self.messagePayload[self.offset + 1])
        self.offset += 2
        return result

    def readInt24(self):
        self.bitoffset = 0
        result = (self.messagePayload[self.offset] << 16)
        result += (self.messagePayload[self.offset + 1] << 8)
        result += (self.messagePayload[self.offset + 2])
        self.offset += 3
        return result

    def readInt(self):
        self.bitoffset = 0
        result = (self.messagePayload[self.offset] << 24)
        result += (self.messagePayload[self.offset + 1] << 16)
        result += (self.messagePayload[self.offset + 2] << 8)
        result += (self.messagePayload[self.offset + 3])
        self.offset += 4
        return result

    def readIntLittleEndian(self):
        self.bitoffset = 0
        result = (self.messagePayload[self.offset])
        result += (self.messagePayload[self.offset + 1] << 8)
        result += (self.messagePayload[self.offset + 2] << 16)
        result += (self.messagePayload[self.offset + 3] << 24)
        self.offset += 4
        return result

    def readLong(self, logicLong=None):
        if not logicLong:
            logicLong = LogicLong(0, 0)
        logicLong.decode(self)
        return [logicLong.high, logicLong.low]

    def readLongLong(self):
        self.bitoffset = 0
        high = (self.messagePayload[self.offset] << 24)
        high += (self.messagePayload[self.offset + 1] << 16)
        high += (self.messagePayload[self.offset + 2] << 8)
        high += (self.messagePayload[self.offset + 3])
        self.offset += 4
        low = (self.messagePayload[self.offset] << 24)
        low += (self.messagePayload[self.offset + 1] << 16)
        low += (self.messagePayload[self.offset + 2] << 8)
        low += (self.messagePayload[self.offset + 3])
        self.offset += 4
        return LogicLong.toLong(high, low)

    def readShort(self):
        self.bitoffset = 0
        result = (self.messagePayload[self.offset] << 8)
        result += (self.messagePayload[self.offset + 1])
        self.offset += 2
        return result

    def readString(self, max=900000):
        self.bitoffset = 0
        length = (self.messagePayload[self.offset] << 24)
        length += (self.messagePayload[self.offset + 1] << 16)
        length += (self.messagePayload[self.offset + 2] << 8)
        length += (self.messagePayload[self.offset + 3])
        self.offset += 4
        if length <= -1:
            if length != -1:
                Debugger.warning("Negative String length encountered.")
            return b''
        elif length > max:
            Debugger.warning(f"Too long String encountered, length {length}, max {max}")
            return b''
        result = bytes(self.messagePayload[self.offset:self.offset + length]).decode('utf-8')
        self.offset += length
        return result

    def readStringReference(self, max):
        self.bitoffset = 0
        length = (self.messagePayload[self.offset] << 24)
        length += (self.messagePayload[self.offset + 1] << 16)
        length += (self.messagePayload[self.offset + 2] << 8)
        length += (self.messagePayload[self.offset + 3])
        self.offset += 4
        if length <= -1:
            if length != -1:
                Debugger.warning("Negative String length encountered.")
            return b''
        elif length > max:
            Debugger.warning(f"Too long String encountered, length {length}, max {max}")
            return b''
        result = self.messagePayload[self.offset].decode('utf-8')
        self.offset += length
        return result

    def readVInt(self):
        offset = self.offset
        self.bitoffset = 0
        v4 = offset + 1
        self.offset = offset + 1
        result = self.messagePayload[offset] & 0x3F
        if (self.messagePayload[offset] & 0x40) != 0:
            if (self.messagePayload[offset] & 0x80) != 0:
                self.offset = offset + 2
                v7 = self.messagePayload[v4]
                v8 = result & 0xFFFFE03F | ((v7 & 0x7F) << 6)
                if (v7 & 0x80) != 0:
                    self.offset = offset + 3
                    v9 = v8 & 0xFFF01FFF | ((self.messagePayload[offset + 2] & 0x7F) << 13)
                    if (self.messagePayload[offset + 2] & 0x80) != 0:
                        self.offset = offset + 4
                        v10 = v9 & 0xF80FFFFF | ((self.messagePayload[offset + 3] & 0x7F) << 20)
                        if (self.messagePayload[offset + 3] & 0x80) != 0:
                            self.offset = offset + 5
                            return v10 & 0x7FFFFFF | (self.messagePayload[offset + 4] << 27) | 0x80000000
                        else:
                            return v10 | 0xF8000000
                    else:
                        return v9 | 0xFFF00000
                else:
                    return v8 | 0xFFFFE000
            else:
                return self.messagePayload[offset] | 0xFFFFFFC0
        elif (self.messagePayload[offset] & 0x80) != 0:
            self.offset = offset + 2
            v6 = self.messagePayload[v4]
            result = result & 0xFFFFE03F | ((v6 & 0x7F) << 6)
            if (v6 & 0x80) != 0:
                self.offset = offset + 3
                result = result & 0xFFF01FFF | ((self.messagePayload[offset + 2] & 0x7F) << 13)
                if (self.messagePayload[offset + 2] & 0x80) != 0:
                    self.offset = offset + 4
                    result = result & 0xF80FFFFF | ((self.messagePayload[offset + 3] & 0x7F) << 20)
                    if (self.messagePayload[offset + 3] & 0x80) != 0:
                        self.offset = offset + 5
                        return result & 0x7FFFFFF | (self.messagePayload[offset + 4] << 27)

        return result

    def readVLong(self):
        result = []
        result.append(self.readVInt())
        result.append(self.readVInt())
        return result

    def removeByteArray(self):
        self.messagePayload = b''

    def reset(self):
        self.length = 0
        self.offset = 0

    def resetOffset(self):
        self.offset = 0
        self.bitoffset = 0

    def rewind(self):
        self.bitoffset = 0
        length = self.length
        if self.length <= self.offset:
            length = self.offset
        self.offset = 0
        self.length = length

    def setOffset(self, offset, bitoffset):
        self.offset = offset
        self.bitoffset = bitoffset

    def skip(self, bytes_to_skip):
        self.bitoffset = 0
        self.offset = self.offset + bytes_to_skip

    def writeBoolean(self, value):
        ChecksumEncoder.writeBoolean(self, value & 1)
        tempBuf = list(self.messagePayload)
        if self.bitoffset == 0:
            offset = self.offset
            self.offset += 1
            tempBuf.append(0)
        if (value & 1) != 0:
            tempBuf[self.offset - 1] = tempBuf[self.offset - 1] | 1 << (self.bitoffset & 31)
        self.bitoffset = self.bitoffset + 1 & 7
        self.messagePayload = bytes(tempBuf)

    def writeByte(self, value):
        ChecksumEncoder.writeByte(self, value)
        self.bitoffset = 0
        tempBuf = list(self.messagePayload)
        tempBuf.append(value & 0xFF)
        self.messagePayload = bytes(tempBuf)
        self.offset += 1

    def writeBytes(self, value, length):
        ChecksumEncoder.writeBytes(self, value, length)
        self.bitoffset = 0
        if value != 0:
            ByteStream.writeIntToByteArray(self, length)
            self.messagePayload += value
            self.offset += length
        else:
            ByteStream.writeIntToByteArray(self, -1)

    def writeInt8(self, value):
        ChecksumEncoder.writeInt(self, value)
        self.bitoffset = 0
        tempBuf = list(self.messagePayload)
        tempBuf.append(value & 0xFF)
        self.messagePayload = bytes(tempBuf)
        self.offset += 1
        
    def writeInt16(self, value):
        ChecksumEncoder.writeInt(self, value)
        self.bitoffset = 0
        tempBuf = list(self.messagePayload)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.messagePayload = bytes(tempBuf)
        self.offset += 2

    def writeInt24(self, value):
        ChecksumEncoder.writeInt(self, value)
        self.bitoffset = 0
        tempBuf = list(self.messagePayload)
        tempBuf.append(value >> 16 & 0xFF)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.messagePayload = bytes(tempBuf)
        self.offset += 3

    def writeInt(self, value):
        ChecksumEncoder.writeInt(self, value)
        ByteStream.writeIntToByteArray(self, value)

    def writeIntLittleEndian(self, value):
        self.bitoffset = 0
        tempBuf = list(self.messagePayload)
        tempBuf.append(value & 0xFF)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value >> 16 & 0xFF)
        tempBuf.append(value >> 24 & 0xFF)
        self.messagePayload = bytes(tempBuf)
        self.offset += 4

    def writeIntToByteArray(self, value):
        self.bitoffset = 0
        tempBuf = list(self.messagePayload)
        tempBuf.append(value >> 24 & 0xFF)
        tempBuf.append(value >> 16 & 0xFF)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.messagePayload = bytes(tempBuf)
        self.offset += 4

    def writeLongLong(self, longlong):
        ChecksumEncoder.writeLongLong(self, longlong)
        self.bitoffset = 0
        high = LogicLong.getHigherInt(longlong)
        ByteStream.writeIntToByteArray(self, high)
        low = LogicLong.getLowerInt(longlong)
        ByteStream.writeIntToByteArray(self, low)

    def writeLong(self, high, low):
        self.writeIntToByteArray(high)
        self.writeIntToByteArray(low)

    def writeShort(self, value):
        ChecksumEncoder.writeShort(self, value)
        self.bitoffset = 0
        tempBuf = list(self.messagePayload)
        tempBuf.append(value >> 8 & 0xFF)
        tempBuf.append(value & 0xFF)
        self.messagePayload = bytes(tempBuf)
        self.offset += 2

    def writeString(self, value=None):
        ChecksumEncoder.writeString(self, value)
        self.bitoffset = 0
        if value != None:
            str_bytes = LogicStringUtil.getBytes(value)
            str_length = LogicStringUtil.getByteLength(str_bytes)
            if str_length < 900001:
                ByteStream.writeIntToByteArray(self, str_length)
                self.messagePayload += str_bytes
                self.offset += str_length
            else:
                Debugger.warning(f"ByteStream::writeString invalid string length {str_length}")
                ByteStream.writeIntToByteArray(self, -1)
        else:
            ByteStream.writeIntToByteArray(self, -1)

    def writeStringReference(self, value):
        ChecksumEncoder.writeStringReference(self, value)
        self.bitoffset = 0
        str_bytes = LogicStringUtil.getBytes(value)
        str_length = LogicStringUtil.getByteLength(str_bytes)
        if str_length < 900001:
            ByteStream.writeIntToByteArray(self, str_length)
            self.messagePayload += str_bytes
            self.offset += str_length
        else:
            Debugger.warning(f"ByteStream::writeString invalid string length {str_length}")
            ByteStream.writeIntToByteArray(self, -1)

    def writeVInt(self, data):
        self.bitoffset = 0
        if type(data) == str:
            data = int(data)
        final = b''
        if (data & 2147483648) != 0:
            if data >= -63:
                final += (data & 0x3F | 0x40).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif data >= -8191:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif data >= -1048575:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif data >= -134217727:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5
        else:
            if data <= 63:
                final += (data & 0x3F).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif data <= 8191:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif data <= 1048575:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif data <= 134217727:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5

        self.messagePayload += final

    def writeVLong(self, high, low):
        ChecksumEncoder.writeVLong(self, high, low)
        self.bitoffset = 0
        self.writeVInt(high)
        self.writeVInt(low)

    def writeCompressedString(self, data):
        self.bitoffset = 0
        compressedText = zlib.compress(data)
        self.writeInt(len(compressedText) + 4)
        self.writeIntLittleEndian(len(data))
        self.messagePayload += compressedText

    def readCompressedString(self):
        data_length = self.readInt()
        self.readIntLittleEndian()
        return zlib.decompress(self.readBytes(data_length - 4))

    #region ByteStreamHelper lazy call

    def readDataReference(self):
        return ByteStreamHelper.readDataReference(self)

    def writeDataReference(self, high=0, low=-1):
        ByteStreamHelper.writeDataReference(self, high, low)

    def decodeIntList(self):
        return ByteStreamHelper.decodeIntList(self)

    def encodeIntList(self, intList):
        ByteStreamHelper.encodeIntList(self, intList)

    def decodeLogicLong(self, logicLong=None):
        return ByteStreamHelper.decodeLogicLong(self, logicLong)

    def encodeLogicLong(self, logicLong):
        ByteStreamHelper.encodeLogicLong(self, logicLong)

    def decodeLogicLongList(self):
        return ByteStreamHelper.decodeLogicLongList(self)

    def encodeLogicLongList(self, logicLongList):
        ByteStreamHelper.encodeLogicLongList(self, logicLongList)

    #endregion