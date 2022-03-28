import os
import Configuration
from Classes.ServerConnection import ServerConnection
from Static.StaticData import StaticData

if not os.path.exists(f"HexDumpV{Configuration.settings['DumpMajor']}"):
    os.mkdir(f"HexDumpV{Configuration.settings['DumpMajor']}")

StaticData.Preload()

ServerConnection(("0.0.0.0", 9339))