import json
import os
import time

import Configuration


class Utility:
    def parseFields(fields: dict):
        print()
        for typeName,value in fields.items():
            print(f"{typeName}: {value}")
        print()

    def dumpPacket(buffer, packetID):
        from Classes.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
        packet_name = LogicLaserMessageFactory.getMessageName(packetID)
        if (packetID not in Configuration.settings["Blacklist"] and len(buffer) != 0):
            if (not os.path.exists(f"HexDumpV{Configuration.settings['DumpMajor']}/" + packet_name)):
                os.mkdir(f"HexDumpV{Configuration.settings['DumpMajor']}/" + packet_name)

            with open((f'HexDumpV{Configuration.settings["DumpMajor"]}/' + packet_name + '/' + str(time.time()) + '_' + packet_name + '.bin'), 'wb') as packet_file:
                packet_file.write(buffer)
                packet_file.close()

    def getContentUpdaterInfo():
        return open(f"./ContentUpdater/lastversion.txt", 'r').read().split('...')

    def getFingerprintData(resourceSha):
        return json.dumps(json.loads(open(f"./ContentUpdater/Update/{resourceSha}/fingerprint.json", 'r').read()))
