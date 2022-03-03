from Classes.CPPDefs import CPPDefs
from Classes.Debugger import Debugger
from Classes.Logic.LogicLong import LogicLong


class ChecksumEncoder:
    def __init__(self):
        self.checksum = 0
        self.checksum2 = 0
        self.checksumEnabled = True

    def destruct(self):
        self.checksum = 0
        self.checksum2 = 0
        self.checksumEnabled = True

    def enableCheckSum(self, state):
        if not self.checksumEnabled or state:
            if not self.checksumEnabled and state:
                self.checksum = self.checksum2
            self.checksumEnabled = state
        else:
            self.checksum2 = self.checksum
            self.checksumEnabled = False

    def equals(self, checksum_instance):
        if not checksum_instance:
            return False

        if not checksum_instance.checksumEnabled:
            checksum = checksum_instance.checksum
        else:
            checksum2 = checksum_instance.checksum2

        if not self.checksumEnabled:
            checksum = self.checksum
        else:
            checksum2 = self.checksum2
        return checksum == checksum2

    def getCheckSum(self):
        if not self.checksumEnabled:
            checksum = self.checksum2
        else:
            checksum = self.checksum
        return checksum

    @staticmethod
    def hashCode():
        Debugger.error("ChecksumEncoder hashCode not designed")
        return 42

    @staticmethod
    def isByteStream():
        return False

    def isCheckSumEnabled(self):
        return self.checksumEnabled

    @staticmethod
    def isCheckSumOnlyMode():
        return True

    def resetCheckSum(self):
        self.checksum = 0

    def writeBoolean(self, value):
        if value: integer = 13
        else: integer = 7
        self.checksum = integer + CPPDefs.__ROR4__(self.checksum, 31)

    def writeByte(self, value):
        self.checksum = CPPDefs.__ROR4__(self.checksum, 31) + value + 11

    def writeBytes(self, value, length):
        if value: integer = length + 38
        else: integer = 37
        self.checksum = CPPDefs.__ROR4__(self.checksum, 31)

    def writeInt8(self, value):
        if value + 0x80 >= 0x100:
            Debugger.error("")
        self.checksum = CPPDefs.__ROR4__(self.checksum, 31) + value + 11

    def writeInt16(self, value):
        if value + 0x8000 >= 0x10000:
            Debugger.error("")
        self.checksum = CPPDefs.__ROR4__(self.checksum, 31) + value + 19

    def writeInt24(self, value):
        if value + 0x800000 >= 0x1000000:
            Debugger.error("")
        self.checksum = (value & 0xFFFFFF) + CPPDefs.__ROR4__(self.checksum, 31) + value + 21

    def writeInt(self, value):
        self.checksum = CPPDefs.__ROR4__(self.checksum, 31) + value + 9

    @staticmethod
    def writeLong(bytestream, logicLong):
        logicLong.encode(bytestream)

    def writeLongLong(self, logicLong):
        self.checksum = logicLong.getLowerInt() + CPPDefs.__ROR4__(logicLong.getHigherInt() + CPPDefs.__ROR4__(self.checksum, 31) + 67, 31) + 91

    def writeShort(self, value):
        self.checksum = CPPDefs.__ROR4__(self.checksum, 31) + value + 19

    def writeString(self, value):
        checksum = CPPDefs.__ROR4__(self.checksum, 31)
        if value:
            self.checksum = checksum + len(value) + 28
        else:
            self.checksum = checksum + 27

    def writeStringReference(self, value):
        self.checksum = len(value) + CPPDefs.__ROR4__(self.checksum, 31) + 38

    def writeVInt(self, value):
        self.checksum = value + CPPDefs.__ROR4__(self.checksum, 31) + 33

    def writeVLong(self, high, low):
        self.checksum = low + CPPDefs.__ROR4__(high + CPPDefs.__ROR4__(self.checksum, 31) + 65, 31) + 88