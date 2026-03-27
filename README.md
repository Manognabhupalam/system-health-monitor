# System Health Monitoring Service

## 📌 Overview

This project implements a UDP-based distributed system to monitor system health metrics (CPU, RAM, Disk) from multiple nodes and display them on a central dashboard.

## ⚙️ Features

* Real-time system monitoring
* Multi-client UDP communication
* Threshold-based alerts
* Offline node detection
* GUI dashboard using Tkinter

## 🛠️ Technologies Used

* Python
* UDP Sockets
* Tkinter
* psutil

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the server

```bash
python server.py
```

### 3. Run clients (in separate terminals)

```bash
python client.py Node1
python client.py Node2
python client.py Node3
```

## 📊 Output

* Displays system health of all nodes
* Shows alerts when thresholds are exceeded
* Detects offline nodes

## 📌 Author

Your Name
