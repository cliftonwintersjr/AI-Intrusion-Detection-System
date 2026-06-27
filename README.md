# AI-Driven Intrusion Detection System

An AI-powered Intrusion Detection System (IDS) that simulates a telecommunications network and detects anomalous traffic using unsupervised machine learning. The project demonstrates how modern security operations can combine machine learning, database logging, real-time alerting, and web visualization into a complete cybersecurity pipeline.

---

## Overview

Traditional Intrusion Detection Systems often rely on known attack signatures, making them less effective against previously unseen threats. This project explores an alternative approach by using **Isolation Forest**, an unsupervised machine learning algorithm, to identify abnormal network behavior without requiring labeled attack data.

The system simulates network traffic commonly found in enterprise or telecommunications environments, analyzes each event for anomalies, stores security events in a MySQL database, generates email notifications, and displays alerts through a Flask web dashboard.

---

## Features

* AI-based anomaly detection using Isolation Forest
* Synthetic telecom network traffic generation
* Real-time intrusion detection pipeline
* Automatic severity classification
* Email alert notifications
* MySQL-backed alert logging
* Flask web dashboard for monitoring
* Modular architecture for future expansion

---

## System Architecture

```text
                Synthetic Traffic Generator
                           │
                           ▼
               Isolation Forest ML Model
                           │
                           ▼
               Real-Time Detection Engine
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Email Notifications   MySQL Database   Flask Dashboard
```

---

## Technologies Used

| Category                | Technology                      |
| ----------------------- | ------------------------------- |
| Language                | Python 3.11                     |
| Machine Learning        | scikit-learn (Isolation Forest) |
| Data Processing         | pandas                          |
| Model Serialization     | joblib                          |
| Database                | MySQL                           |
| Email Notifications     | SMTP (smtplib)                  |
| Web Framework           | Flask                           |
| Development Environment | VS Code                         |
| Operating System        | macOS                           |

---

## Project Structure

```text
AI-Intrusion-Detection-System/
│
├── data_generator.py        # Generates synthetic telecom traffic
├── model_training.py        # Trains Isolation Forest model
├── alert_system.py          # Performs anomaly detection
├── database.py              # Database interface
├── dashboard.py             # Flask dashboard
│
├── telecom_traffic.csv      # Generated training data
├── ai_ids_model.pkl         # Trained ML model
│
├── templates/
│   └── dashboard.html
│
├── requirements.txt
└── README.md
```

---

## How It Works

### 1. Traffic Generation

The project begins by creating thousands of simulated network connections representing normal telecommunications traffic. Features include:

* Packet size
* Connection duration
* Packets per second
* Failed connection attempts
* Data transfer rate
* Connection attempts

The generator can also simulate abnormal traffic patterns similar to high-volume attacks such as Distributed Denial of Service (DDoS).

---

### 2. Machine Learning

The generated dataset is used to train an **Isolation Forest** model.

Unlike supervised classifiers, Isolation Forest learns what normal behavior looks like and flags observations that differ significantly from expected patterns.

Model parameters include:

* 200 decision trees
* 5% contamination rate
* Fixed random seed for reproducibility

The trained model is serialized using **joblib** for later use by the detection engine.

---

### 3. Detection Engine

Incoming traffic is evaluated by the trained model.

When anomalous behavior is detected, the system:

* Classifies the event
* Assigns a severity level
* Records network metadata
* Creates a security alert
* Stores the alert in MySQL
* Sends an email notification
* Makes the alert available on the dashboard

---

### 4. Alert Logging

Detected events are stored in a MySQL database with information such as:

* Timestamp
* Attack type
* Severity
* Description
* Packet statistics
* Connection metrics

Persistent storage enables future analysis and forensic investigation.

---

### 5. Dashboard

A lightweight Flask web application retrieves stored alerts from the database and displays them through a browser-based interface.

The dashboard provides a centralized location for monitoring detected anomalies and reviewing historical security events.

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Intrusion-Detection-System.git

cd AI-Intrusion-Detection-System
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Configure MySQL

Create a database named:

```sql
CREATE DATABASE ai;
```

Create the `alerts` table and update the database credentials in `database.py`.

---

### Generate Sample Traffic

```bash
python3 data_generator.py
```

---

### Train the Model

```bash
python3 model_training.py
```

---

### Start the Detection Engine

```bash
python3 alert_system.py
```

---

### Launch the Dashboard

```bash
python3 dashboard.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## Example Workflow

```text
Generate Network Traffic
          │
          ▼
Train Isolation Forest
          │
          ▼
Analyze Incoming Events
          │
          ▼
Anomaly Detected
          │
          ▼
Store in Database
          │
          ├──► Email Notification
          │
          └──► Flask Dashboard
```

---

## Skills Demonstrated

* Machine Learning for Cybersecurity
* Intrusion Detection Systems
* Security Monitoring
* Python Development
* Database Design
* Flask Web Applications
* MySQL Integration
* Email Automation
* Data Processing
* Software Architecture
* Modular Software Design

---

## Current Limitations

* Uses synthetic network traffic rather than production data
* Simplified feature engineering
* Basic web interface
* No automated incident response
* Single anomaly detection algorithm

---

## Future Improvements

* Real-time packet capture integration
* Kafka event streaming pipeline
* Interactive Plotly dashboards
* MITRE ATT&CK mapping
* Geo-IP enrichment
* Threat intelligence integration
* Docker deployment
* REST API
* Unit and integration testing
* CI/CD with GitHub Actions

---

## Author

**Clifton Winters Jr.**

Computer Science – Cybersecurity

This project was created to demonstrate practical applications of artificial intelligence, machine learning, and software engineering principles within modern cybersecurity environments.
