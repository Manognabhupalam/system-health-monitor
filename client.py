import socket
import psutil
import time
import sys

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

node_name = sys.argv[1] if len(sys.argv) > 1 else "Node"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    message = f"{node_name}|CPU:{cpu}|RAM:{ram}|DISK:{disk}"

    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    print("Sent:", message)

    time.sleep(5)