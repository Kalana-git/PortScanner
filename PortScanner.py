import socket
from datetime import datetime
import pyfiglet

def Big_banner(text, font="standard"):
    banner = pyfiglet.figlet_format(text, font=font)
    print(banner)

def Small_banner(text, font="small"):
    banner = pyfiglet.figlet_format(text, font=font)
    print(banner)

print("-"*70)

Big_banner("Port Scanner", font="slant")
Small_banner("Created by Kalana", font="mini")

print("-"*70)

start_port = 1
end_port = 1024

targetIP = input("Enter the target IP address: ")

print(f"Scan Target: {targetIP}")
print(f"Scanning started: {datetime.now()}")

try:
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((targetIP, port))

        if result == 0:
            print("Port {port} is open.")

        sock.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    exit()

except socket.error:

    print("Couldn't connect to the server.")
