from typing import overload


class LogicLong:
    def __init__(self):
        self.high = 0
        self.low = 0

    def __init__(self, high, low):
        self.high = high
        self.low = low

    @staticmethod
    def clone(logicLong):
        return LogicLong(logicLong.high, logicLong.low)

    def decode(self, bytestream):
        self.high = bytestream.readInt()
        self.low = bytestream.readInt()

    def encode(self, bytestream):
        bytestream.writeInt(self.high)
        bytestream.writeInt(self.low)

    def equals(self, logicLong):
        if logicLong:
            if self.low == logicLong.low:
                return self.high == logicLong.high
        return False

    @staticmethod
    def getHigherInt(longlong):
        return longlong >> 32

    @overload
    def getHigherInt(self):
        return self.high

    @staticmethod
    def getLowerInt(longlong):
        result = longlong & 0x7FFFFFFF
        if longlong < 0:
            return longlong | 0x80000000
        return result

    @overload
    def getLowerInt(self):
        return self.low

    def getLong(self):
        result = self.low
        if result >> 31 == -1:
            return result | 0x80000000
        return result

    def greaterThan(self, logicLong):
        result = False
        if logicLong:
            result = True
            if self.high <= logicLong.high:
                result = False
                if self.high == logicLong.high:
                    return self.low > logicLong.low
        return result

    def hashCode(self):
        return 31 * self.high + self.low

    def isZero(self):
        if not self.low:
            return self.high == 0
        else:
            return False

    def set(self, low, high):
        lowerInt = low & 0x7FFFFFFF
        if low < 0:
            lowerInt = low | 0x80000000
        self.high = high >> 32
        self.low = lowerInt

    def toLong(high, low):
        lowerInt = low & 0x7FFFFFFF
        if low < 0:
            lowerInt = low | 0x80000000
        return lowerInt | high << 32

    def toString(text, logiclong):
        print(text, f"LogicLong({logiclong.high},{logiclong.low})")