import os
import Configuration
from Classes.ServerConnection import ServerConnection

if not os.path.exists(f"HexDumpV{Configuration.settings['DumpMajor']}"):
    os.mkdir(f"HexDumpV{Configuration.settings['DumpMajor']}")

ServerConnection(("0.0.0.0", 9339))