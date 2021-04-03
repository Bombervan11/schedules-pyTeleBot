
import os
import subprocess
import sys
from colorama import init, Fore, Back, Style
import time
x = 0
init()

def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    print("██╗  ██╗██╗████████╗███████╗███╗   ██╗ █████╗ ██╗   ██╗██████╗  ██████╗ ████████╗")
    time.sleep(0.1)
    print("██║ ██╔╝██║╚══██╔══╝╚══███╔╝████╗  ██║██╔══██╗██║   ██║██╔══██╗██╔═══██╗╚══██╔══╝")
    time.sleep(0.1)
    print("█████╔╝ ██║   ██║     ███╔╝ ██╔██╗ ██║███████║██║   ██║██████╔╝██║   ██║   ██║   ")
    time.sleep(0.1)
    print("██╔═██╗ ██║   ██║    ███╔╝  ██║╚██╗██║██╔══██║██║   ██║██╔══██╗██║   ██║   ██║   ")
    time.sleep(0.1)
    print("██║  ██╗██║   ██║   ███████╗██║ ╚████║██║  ██║╚██████╔╝██████╔╝╚██████╔╝   ██║   ")
    time.sleep(0.1)
    print("╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   ")
    time.sleep(0.1)
    print("                                                                                 ")
    time.sleep(0.2)
console_picture()
print("Press Enter to start...")
input()

while (True):
    x = x + 1
    print('Launching №',(x))
    process = subprocess.Popen([sys.executable, "Bot.py"])
    process.wait()
