print("ALERT SYSTEM STARTED")

import pandas as pd # type: ignore
import random
import joblib # type: ignore
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from database import insert_alert

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("ai_ids_model.pkl")

features = [
    "packet_size",
    "connection_duration",
    "packets_per_second",
    "failed_connections",
    "data_transfer_rate",
    "connection_attempts"
]

# -----------------------------
# Gmail Configuration
# -----------------------------
SENDER_EMAIL = "cliftonwintersjr@gmail.com"
APP_PASSWORD = "bmju pgnv gpap lifn"   # Gmail App Password (NOT normal password)
RECEIVER_EMAIL = "cliftonwintersjr@gmail.com"

# -----------------------------
# Send Email Function
# -----------------------------
def send_email_alert(alert_text, subject):
    msg = MIMEText(alert_text)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        print("📧 Email alert sent successfully!")

    except Exception as e:
        print("❌ Email failed:", e)

# -----------------------------
# Attack Classification
# -----------------------------
def classify_attack(row):
    if row["packets_per_second"] > 4000:
        return "DDoS Attack"

    elif row["connection_attempts"] > 250:
        return "Port Scan"

    elif row["failed_connections"] > 300:
        return "Credential Stuffing"

    elif row["data_transfer_rate"] > 8000:
        return "Data Exfiltration"

    else:
        return "Unknown Anomaly"

# -----------------------------
# Severity Mapping
# -----------------------------
def get_severity(attack_type):
    if attack_type in ["DDoS Attack", "Data Exfiltration"]:
        return "CRITICAL"
    elif attack_type == "Credential Stuffing":
        return "HIGH"
    elif attack_type == "Port Scan":
        return "MEDIUM"
    else:
        return "LOW"

# -----------------------------
# Alert Builder
# -----------------------------
def generate_alert(row, attack_type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    severity = get_severity(attack_type)

    subject = f"🚨 AI IDS ALERT - {attack_type} ({severity})"

    alert_message = f"""
=====================================
AI-DRIVEN IDS ALERT
=====================================

Timestamp: {timestamp}

Threat Type: {attack_type}
Severity: {severity}

Description:
An anomaly was detected in simulated telecom network traffic.
This behavior deviates from normal baseline patterns learned by the ML model.

--- Network Metrics ---
Packet Size: {row['packet_size']}
Packets/sec: {row['packets_per_second']}
Connection Duration: {row['connection_duration']}
Failed Connections: {row['failed_connections']}
Data Transfer Rate: {row['data_transfer_rate']}
Connection Attempts: {row['connection_attempts']}

--- Recommended Response ---
- Investigate source traffic
- Review firewall / IDS logs
- Apply rate limiting if needed
- Check for persistence or repeated patterns

=====================================
"""

    print(alert_message)

    # Send email alert
    send_email_alert(alert_message, subject)

    alert_data = {
    "timestamp": timestamp,
    "attack_type": attack_type,
    "severity": severity,
    "description": "AI-detected anomaly in telecom traffic",
    "packet_size": row["packet_size"],
    "packets_per_second": row["packets_per_second"],
    "connection_duration": row["connection_duration"],
    "failed_connections": row["failed_connections"],
    "data_transfer_rate": row["data_transfer_rate"],
    "connection_attempts": row["connection_attempts"]
}
    insert_alert(alert_data)

# -----------------------------
# Simulated Real-Time Traffic
# -----------------------------
def simulate_traffic():
    return {
        "packet_size": random.randint(50, 1500),
        "connection_duration": random.uniform(0.1, 10),
        "packets_per_second": random.randint(50, 6000),
        "failed_connections": random.randint(0, 500),
        "data_transfer_rate": random.uniform(50, 12000),
        "connection_attempts": random.randint(10, 500)
    }

# -----------------------------
# Main Loop (Real-Time Detection)
# -----------------------------
print("Running real-time detection...\n")

for i in range(20):
    row = simulate_traffic()
    df = pd.DataFrame([row])

    prediction = model.predict(df)[0]

    if prediction == -1:
        attack_type = classify_attack(row)
        generate_alert(row, attack_type)
    else:
        print(f"[{i}] Normal traffic detected")

print("\nALERT SYSTEM FINISHED")