# 🌟 AIOps Lab: CPU Anomaly Detection 🌟

*Created by CLOUDHIRED OFFICIAL*

Welcome to the **AIOps Lab**, a powerful tool for monitoring CPU usage and detecting anomalies using **Prometheus, Grafana, and Machine Learning**! This project is designed to help you set up a **production-ready monitoring system** with ease.

---

## ✨ Features

- 🚀 **Real-time Monitoring**: Track CPU usage with **Prometheus** and **Node Exporter**.
- 🔍 **Anomaly Detection**: Uses **Isolation Forest** to detect unusual CPU patterns.
- 📊 **Visualization**: Beautiful, interactive dashboards with **Grafana**.
- 🔔 **Alerts**: Get notified via **Slack** when anomalies occur.
- 🛠 **Easy Setup**: One-command **Docker deployment**.

---

## 📋 Prerequisites

Before you begin, ensure you have:

- 🐳 **Docker** & **Docker Compose** installed
- 🐍 **Python 3.8+**
- 🌐 **Git** (optional, for cloning the repo)
- 💬 **Slack Webhook URL** (optional, for alerts)

---

## 🚀 Quick Start Guide

### Step 1: Set Up the Environment

```bash
# Clone the repository (optional)
git clone https://github.com/yourusername/aiops-lab.git
cd aiops-lab

# Install Docker dependencies (if not already installed)
sudo apt-get update
sudo apt-get install -y docker.io docker-compose

# Install Python dependencies
pip install -r scripts/requirements.txt

# Install additional dependencies
pip install pandas requests scikit-learn
```

### Step 2: Launch the Monitoring Stack

```bash
docker-compose up -d
```

### Step 3: Run the AIOps Pipeline

```bash
cd scripts
python3 fetch_metrics.py    # Collect 6 hours of CPU data
python3 train_model.py      # Train the anomaly detection model
python3 detect_anomalies.py # Start real-time monitoring
```

### Step 4: Test the System

```bash
# Install stress-ng (Ubuntu/Debian)
sudo apt-get install -y stress-ng

# Simulate CPU load
stress-ng --cpu 2 --timeout 120s
```

---

## 🎨 Visualization

- **Prometheus**: Visit 👉 [http://localhost:9090](http://localhost:9090)
- **Grafana**: Go to 👉 [http://localhost:3000](http://localhost:3000) (**default login**: admin/admin)
- **Add Prometheus Datasource**: `http://prometheus:9090`
- **Import Dashboard ID**: `1860 (Node Exporter Full)`

---

## 🔔 Slack Notifications

1. **Create a Slack webhook**: [Slack Webhooks Guide](https://api.slack.com/messaging/webhooks)
2. **Edit `scripts/config.ini`** and replace `YOUR_SLACK_WEBHOOK_URL` with your webhook URL.

---

## 🛠️ Troubleshooting

- 🔄 **Check Docker**: `docker ps` (ensure all services are running)
- 📜 **View Logs**: `docker-compose logs`
- 📊 **Data Issues**: Verify `cpu_metrics.csv` exists and contains data

---

## 🎉 Credits

Developed by **CLOUDHIRED OFFICIAL** © 2026. All rights reserved.

Enjoy your AIOps journey! 🚀




================================================V2========================

# AIOps • MLOps • DevOps Labs 🚀

**Created by CLOUDHIRED OFFICIAL**

Welcome to the AIOps • MLOps • DevOps Labs repository.

This repository contains hands-on real-world projects covering:

* AIOps
* MLOps
* DevOps
* Cloud Engineering
* Kubernetes
* OpenShift
* Platform Engineering
* Site Reliability Engineering (SRE)

---

# 📁 Repository Structure

```text
DAY-01
└── AIOps Lab: CPU Anomaly Detection

DAY-02
└── Coming Soon

DAY-03
└── Coming Soon
```

---

# 🚀 DAY-01: AIOps Lab - CPU Anomaly Detection

This lab demonstrates how to build an AIOps solution using:

* Prometheus
* Grafana
* Node Exporter
* Python
* Isolation Forest
* Slack Webhooks
* Docker Compose
* AWS EC2

---

# ✨ Features

🚀 Real-Time Monitoring

🔍 Machine Learning-Based Anomaly Detection

📊 Grafana Dashboards

🔔 Slack Notifications

🐳 Docker Compose Deployment

☁️ AWS EC2 Deployment

---

# 📋 Prerequisites

Before starting, ensure you have:

* AWS EC2 Instance
* Docker Installed
* Docker Compose Installed
* Python 3.x
* Git
* Slack Webhook URL (Optional)

---

# 🏗 Architecture

```text
Node Exporter
      │
      ▼
Prometheus
      │
      ▼
fetch_metrics.py
      │
      ▼
cpu_metrics.csv
      │
      ▼
train_model.py
      │
      ▼
aiops_model.joblib
      │
      ▼
detect_anomalies.py
      │
      ▼
Isolation Forest
      │
      ▼
Slack Alert
      │
      ▼
Grafana Dashboard
```

---

# 🚀 Step 1: Connect to EC2

```bash
ssh -i your-key.pem ec2-user@<PUBLIC-IP>
```

Example:

```bash
ssh -i aiops.pem ec2-user@54.xxx.xxx.xxx
```

---

# 🚀 Step 2: Install Git

```bash
sudo dnf update -y

sudo dnf install git -y
```

Verify:

```bash
git --version
```

---

# 🚀 Step 3: Clone Repository

```bash
git clone https://github.com/bdreddy738/aiops-mlops-devops-labs.git
```

Navigate to Project

```bash
cd aiops-mlops-devops-labs

cd DAY-01

cd aiops-lab
```

---

# 🚀 Step 4: Activate Python Environment

```bash
source venv/bin/activate
```

Expected:

```text
(venv)
```

Install Dependencies

```bash
pip install -r scripts/requirements.txt
```

Verify Installation

```bash
python3 -c "import pandas,requests,sklearn,joblib; print('OK')"
```

Expected Output

```text
OK
```

---

# 🚀 Step 5: Start Monitoring Stack

Launch Containers

```bash
docker compose up -d
```

Verify

```bash
docker ps
```

Expected

```text
prometheus
grafana
node_exporter
```

---

# 🚀 Step 6: Configure Slack Webhook

Edit Configuration

```bash
vi scripts/config.ini
```

Replace

```ini
slack_webhook = YOUR_SLACK_WEBHOOK_URL
```

With

```ini
slack_webhook = https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX
```

Save File

---

# 🚀 Step 7: Collect Historical Metrics

Move to Scripts Folder

```bash
cd scripts
```

Run

```bash
python3 fetch_metrics.py
```

Expected

```text
✅ Saved 24 metrics to cpu_metrics.csv
```

Generated File

```text
cpu_metrics.csv
```

---

# 🚀 Step 8: Train ML Model

```bash
python3 train_model.py
```

Expected

```text
✅ Model trained and saved as aiops_model.joblib
```

Generated File

```text
aiops_model.joblib
```

---

# 🚀 Step 9: Start Real-Time Detection

```bash
python3 detect_anomalies.py
```

Expected

```text
✅ AIOps detector started. Monitoring CPU...

✅ CPU Normal: 1.20%

✅ CPU Normal: 2.10%
```

---

# 🚀 Step 10: Open Second Terminal

Connect Again

```bash
ssh -i your-key.pem ec2-user@<PUBLIC-IP>
```

Navigate

```bash
cd aiops-mlops-devops-labs/DAY-01/aiops-lab
```

---

# 🚀 Step 11: Install Stress Tool

```bash
sudo dnf install stress-ng -y
```

Verify

```bash
stress-ng --version
```

---

# 🚀 Step 12: Generate CPU Load

```bash
stress-ng --cpu 2 --timeout 120s
```

Purpose

```text
Generate High CPU Usage
```

---

# 🔔 Expected Result

Detector Terminal

```text
🚨 CPU Anomaly Detected: 95.20%

✅ Slack alert sent
```

Slack Channel

```text
🚨 CPU Anomaly Detected: 95.20%
```

---

# 📊 Prometheus

Open Browser

```text
http://<PUBLIC-IP>:9090
```

Purpose

```text
Metrics Collection & Query Engine
```

---

# 📊 Grafana

Open Browser

```text
http://<PUBLIC-IP>:3000
```

Default Credentials

```text
Username: admin

Password: admin
```

---

# 📊 Configure Grafana

Add Data Source

```text
Connections
→ Data Sources
→ Add Data Source
→ Prometheus
```

Prometheus URL

```text
http://prometheus:9090
```

Click

```text
Save & Test
```

Expected

```text
Data source is working
```

---

# 📊 Import Dashboard

Navigate

```text
Dashboards
→ Import
```

Dashboard ID

```text
1860
```

Dashboard Name

```text
Node Exporter Full
```

---

# 📊 Dashboard Metrics

Grafana Displays:

* CPU Usage
* Memory Usage
* Disk Usage
* Network Usage
* Load Average
* Host Statistics

---

# 🛠 Troubleshooting

Check Containers

```bash
docker ps
```

View Logs

```bash
docker compose logs
```

Check Prometheus Targets

```text
http://<PUBLIC-IP>:9090/targets
```

Check Node Exporter

```text
http://<PUBLIC-IP>:9100/metrics
```

---

# 🎯 Learning Outcomes

After completing this lab, you will gain hands-on experience with:

✅ AWS EC2

✅ Docker Compose

✅ Prometheus

✅ Grafana

✅ Node Exporter

✅ Python

✅ Machine Learning

✅ Isolation Forest

✅ Anomaly Detection

✅ Slack Webhooks

✅ AIOps Fundamentals



# 🎉 Developed By

CLOUDHIRED OFFICIAL © 2026

Happy Learning • Happy Monitoring • Happy Automation 🚀
