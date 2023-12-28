import os
import platform
os.system("git pull")

device = platform.architecture()[0]

if device == "64bit":
    if os.path.isfile("ultra.cpython-311.so"):
        try:
            from ultra import main_apv
            main_apv()
        except ImportError:
            print("\nThe script is currently not available due to an update.")
    else:
        os.system("clear")
        print("\nThe script is currently not available due to an update.")
elif device == "32bit":
    os.system("clear")
    print("\nSorry, your device is not supported.")
else:
    os.system("clear")
    print("\nUnknown device architecture. Exiting.")
    exit()
