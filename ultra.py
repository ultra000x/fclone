import os
import platform

device = platform.architecture()[0]

if device == "64bit":
    if os.path.isfile("ultra.cpython-311.so"):
        try:
            from ultra import main_apv
            main_apv()
        except ImportError:
            print("The script is currently not available due to an update.")
    else:
        print("The script is not available. Please check for updates.")
elif device == "32bit":
    os.system("clear")
    print("Sorry, your device is not supported.")
else:
    os.system("clear")
    print("Unknown device architecture. Exiting.")
    exit()
