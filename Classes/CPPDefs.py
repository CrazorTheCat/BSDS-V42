class CPPDefs:
    # region Rotate Left
    @staticmethod
    def rotl8(value, count):
        return value << count | value >> (8 - count)

    @staticmethod
    def rotl16(value, count):
        return value << count | value >> (16 - count)

    @staticmethod
    def rotl32(value, count):
        return value << count | value >> (32 - count)

    @staticmethod
    def rotl64(value, count):
        return value << count | value >> (64 - count)

    @staticmethod
    def __ROL1__(value, count):
        return CPPDefs.rotl8(value, count)

    @staticmethod
    def __ROL2__(value, count):
        return CPPDefs.rotl16(value, count)

    @staticmethod
    def __ROL4__(value, count):
        return CPPDefs.rotl32(value, count)

    @staticmethod
    def __ROL8__(value, count):
        return CPPDefs.rotl64(value, count)
    # endregion

    # region Rotate Right
    @staticmethod
    def rotr8(value, count):
        return value >> count | value << (8 - count)

    @staticmethod
    def rotr16(value, count):
        return value >> count | value << (16 - count)

    @staticmethod
    def rotr32(value, count):
        return value >> count | value << (32 - count)

    @staticmethod
    def rotr64(value, count):
        return value >> count | value << (64 - count)

    @staticmethod
    def __ROR1__(value, count):
        return CPPDefs.rotr8(value, count)

    @staticmethod
    def __ROR2__(value, count):
        return CPPDefs.rotr16(value, count)

    @staticmethod
    def __ROR4__(value, count):
        return CPPDefs.rotr32(value, count)

    @staticmethod
    def __ROR8__(value, count):
        return CPPDefs.rotr64(value, count)
    # endregion