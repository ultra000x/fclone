import os
import platform
from importlib import import_module

device = platform.architecture()[0]

if device == "64bit":
    try:
        ultra_module = import_module("ultra")
        ultra_module.main_apv()
    except ImportError:
        print("The script is currently not available due to an update.")
elif device == "32bit":
    os.system("clear")
    print("Sorry, your device is not supported.")
else:
    os.system("clear")
    print("Unknown device architecture. Exiting.")
    exit()
