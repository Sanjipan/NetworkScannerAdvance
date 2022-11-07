import sys
import socket
import threading
import time

use1 = "python NetworkScanner.py <TARGET> <START_PORT> <END_PORT>"
use2 = "python NetworkScanner.py <TARGET> <PORT>"
use3 = "python NetworkScanner.py <TARGET>"


def Scan_in_Range():
    start_time = time.time()
    if len(sys.argv) != 4:
        print(use1)
        sys.exit()
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Name Resolution Error")
        sys.exit()
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    print("SCANNING TARGET : {} ".format(target))

    # To Scan ports
    def scan_port(port):
        # print("SCANNING PORT:", port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        con = s.connect_ex((target, port))
        if not con:
            print("[*] PORT :{:5} IS OPEN".format(port))
        s.close()

    print("SCANNING STARTED")
    for ports in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ports,))
        thread.start()
    end_time = time.time()
    print("SCANNING COMPLETE")
    print("TIME TAKEN :", end_time - start_time, "s")
    print("=" * 100)
    sys.exit()


def Scan_all_Ports():
    start_time = time.time()
    if len(sys.argv) != 2:
        print(use3)
        sys.exit()
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Name Resolution Error")
        sys.exit()

    start_port = 1
    end_port = 65535

    print("SCANNING TARGET : {} ".format(target))

    # To Scan ports
    def scan_port(port):
        # print("SCANNING PORT:", port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        con = s.connect_ex((target, port))
        if not con:
            print("[*] PORT :{:5} IS OPEN".format(port))
        s.close()

    print("SCANNING STARTED")
    for ports in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ports,))
        thread.start()
    end_time = time.time()
    print("SCANNING COMPLETE")
    print("TIME TAKEN :", end_time - start_time, "s")
    print("=" * 100)
    sys.exit()


def Scan_one_port():
    start_time = time.time()
    if len(sys.argv) != 3:
        print(use2)
        sys.exit()
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Name Resolution Error")
        sys.exit()

    print("SCANNING TARGET : {} ".format(target))
    print("SCANNING STARTED")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    con = s.connect_ex((target, int(sys.argv[2])))
    if not con:
        print("[*] PORT :{:5} IS OPEN".format(sys.argv[2]))
    else:
        print("[*] PORT :{:5} IS NOT OPEN".format(sys.argv[2]))
    s.close()
    end_time = time.time()
    print("SCANNING COMPLETE")
    print("TIME TAKEN :", end_time - start_time, "s")
    print("=" * 100)
    sys.exit()


print("=" * 100)
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠉⠉⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠟⣹⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⡟⢿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⠟⠉⠀⢰⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⡀⠈⠻⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀")
print("⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⣾⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡇⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀")
print("⠀⢠⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣦⠀⠀")
print("⣰⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣷⡄")
print("⠈⠻⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠉⠛⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡏⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⡿⠟⠁")
print("⠀⠀⠘⠻⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⢸⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⠁⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀")
print("⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⢻⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣣⣴⣾⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⢀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(" ______      ____    ______  __  __      ____        __    __  _____   __  __      ")
print("/\__  _\    /\  _`\ /\  _  \/\ \/\ \    /\  _`\     /\ \  /\ \/\  __`\/\ \/\ \     ")
print("\/_/\ \/    \ \ \/\_\ \ \L\ \ \ `\\ \   \ \ \/\_\   \ `\`\\/'/\ \ \/\ \ \ \ \ \    ")
print("   \ \ \     \ \ \/_/\ \  __ \ \ , ` \   \ \ \/_/_   `\ `\ /'  \ \ \ \ \ \ \ \ \   ")
print("    \_\ \__   \ \ \L\ \ \ \/\ \ \ \`\ \   \ \ \L\ \    `\ \ \   \ \ \_\ \ \ \_\ \  ")
print("    /\_____\   \ \____/\ \_\ \_\ \_\ \_\   \ \____/      \ \_\   \ \_____\ \_____\ ")
print("    \/_____/    \/___/  \/_/\/_/\/_/\/_/    \/___/        \/_/    \/_____/\/_____/ ")
print("=" * 100)

while True:
    if len(sys.argv) == 4:
        Scan_in_Range()
    elif len(sys.argv) == 2:
        Scan_all_Ports()
    elif len(sys.argv) == 3:
        Scan_one_port()
    else:
        print("FORMAT:" + use1)
        print("FORMAT:" + use2)
        print("FORMAT:" + use3)
        break
