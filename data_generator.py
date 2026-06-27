print("RUNNING DATA GENERATOR")

import pandas as pd # type: ignore
import random

def generate_normal():
    return {
        "packet_size": random.randint(400, 800),
        "connection_duration": random.uniform(1, 10),
        "packets_per_second": random.randint(100, 500),
        "failed_connections": random.randint(0, 5),
        "data_transfer_rate": random.uniform(100, 500),
        "connection_attempts": random.randint(10, 50),
        "label": "Normal"
    }

def generate_ddos():
    return {
        "packet_size": random.randint(1200, 1500),
        "connection_duration": random.uniform(0.1, 3),
        "packets_per_second": random.randint(4000, 7000),
        "failed_connections": random.randint(50, 200),
        "data_transfer_rate": random.uniform(5000, 10000),
        "connection_attempts": random.randint(300, 800),
        "label": "Attack"
    }

def generate_port_scan():
    return {
        "packet_size": random.randint(40, 100),
        "connection_duration": random.uniform(0.1, 1),
        "packets_per_second": random.randint(1500, 3000),
        "failed_connections": random.randint(20, 80),
        "data_transfer_rate": random.uniform(50, 200),
        "connection_attempts": random.randint(200, 600),
        "label": "Attack"
    }

def generate_credential_attack():
    return {
        "packet_size": random.randint(300, 800),
        "connection_duration": random.uniform(1, 5),
        "packets_per_second": random.randint(500, 1500),
        "failed_connections": random.randint(300, 600),
        "data_transfer_rate": random.uniform(100, 300),
        "connection_attempts": random.randint(500, 1000),
        "label": "Attack"
    }

def generate_exfiltration():
    return {
        "packet_size": random.randint(800, 1400),
        "connection_duration": random.uniform(100, 500),
        "packets_per_second": random.randint(1000, 3000),
        "failed_connections": random.randint(0, 20),
        "data_transfer_rate": random.uniform(7000, 15000),
        "connection_attempts": random.randint(50, 200),
        "label": "Attack"
    }

traffic = []

for _ in range(5000):
    traffic.append(generate_normal())

for _ in range(125):
    traffic.append(generate_ddos())

for _ in range(125):
    traffic.append(generate_port_scan())

for _ in range(125):
    traffic.append(generate_credential_attack())

for _ in range(125):
    traffic.append(generate_exfiltration())

df = pd.DataFrame(traffic)

df.to_csv("telecom_traffic.csv", index=False)

print("Dataset created successfully!")