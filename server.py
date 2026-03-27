import socket
import threading
import time
import tkinter as tk

SERVER_IP = "0.0.0.0"
SERVER_PORT = 9999

# node: (cpu, ram, disk, last_seen_time)
nodes = {}

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("System Health Monitor")
root.geometry("600x400")

title = tk.Label(root, text="SYSTEM HEALTH DASHBOARD", font=("Arial", 16))
title.pack(pady=10)

text_area = tk.Text(root, font=("Consolas", 12))
text_area.pack(expand=True, fill="both")


def update_dashboard():
    while True:
        text_area.delete(1.0, tk.END)

        current_time = time.time()

        output = "===================================\n"
        output += "     SYSTEM HEALTH DASHBOARD\n"
        output += "===================================\n\n"

        for node, data in nodes.items():
            cpu, ram, disk, last_seen = data

            if current_time - last_seen > 10:
                output += f"{node}   OFFLINE\n\n"
            else:
                output += f"{node}   CPU:{cpu}%   RAM:{ram}%   DISK:{disk}%\n"

                if cpu > 80:
                    output += f"⚠ ALERT: {node} CPU HIGH\n"

                if ram > 85:
                    output += f"⚠ ALERT: {node} RAM HIGH\n"

                if disk > 90:
                    output += f"⚠ ALERT: {node} DISK HIGH\n"

                output += "\n"

        output += f"Total Nodes: {len(nodes)}"

        text_area.insert(tk.END, output)

        time.sleep(2)


# ---------------- UDP RECEIVER ---------------- #
def receive_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_IP, SERVER_PORT))

    print("Server started...")

    while True:
        data, addr = sock.recvfrom(1024)

        message = data.decode()
        parts = message.split("|")

        node = parts[0]
        cpu = float(parts[1].split(":")[1])
        ram = float(parts[2].split(":")[1])
        disk = float(parts[3].split(":")[1])

        nodes[node] = (cpu, ram, disk, time.time())


# Run threads
threading.Thread(target=receive_data, daemon=True).start()
threading.Thread(target=update_dashboard, daemon=True).start()

# Start GUI
root.mainloop()