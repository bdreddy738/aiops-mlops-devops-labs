# AIOps Lab – Prometheus, Grafana, Python ML & Slack Integration on AWS EC2

## Overview

This project demonstrates an end-to-end AIOps pipeline using:

* AWS EC2 (Amazon Linux 2023)
* Prometheus
* Grafana
* Node Exporter
* Python
* Scikit-Learn
* Slack Alerts
* Docker & Docker Compose

The solution collects CPU metrics from EC2, trains an ML model, detects anomalies in real time, and sends notifications to Slack when abnormal CPU behavior is detected.

---

# Architecture

EC2 Instance
↓
Node Exporter
↓
Prometheus
↓
Python ML Scripts
↓
Anomaly Detection
↓
Slack Alert
↓
Grafana Dashboard

---

# Prerequisites

* AWS Account
* EC2 Instance (Amazon Linux 2023)
* Security Group Access
* Slack Workspace
* Internet Connectivity

---

# Step 1: Install Git

```bash
sudo dnf update -y
sudo dnf install git -y

git --version
```

Clone repository:

```bash
git clone https://github.com/bdreddy738/aiops-mlops-devops-labs.git

cd aiops-mlops-devops-labs/DAY-01/aiops-lab
```

---

# Step 2: Install Docker

```bash
sudo dnf update -y

sudo dnf install docker -y

sudo systemctl enable docker
sudo systemctl start docker

docker --version
```

Verify:

```bash
systemctl status docker
```
sudo systemctl start docker

Expected:

```text
Active: active (running)
```

---

# Step 3: Install Docker Compose

```bash
mkdir -p ~/.docker/cli-plugins

curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
-o ~/.docker/cli-plugins/docker-compose

chmod +x ~/.docker/cli-plugins/docker-compose
```

Verify:

```bash
docker compose version
```

---

# Step 4: Start Monitoring Stack

```bash
docker compose up -d
```

Verify containers:

```bash
docker ps
```

Expected services:

* Prometheus
* Grafana
* Node Exporter

---

# Step 5: Configure AWS Security Group

Navigate:

AWS Console

EC2
→ Instances
→ Security
→ Security Group
→ Edit Inbound Rules

Add the following rules:

| Type       | Protocol | Port | Source    |
| ---------- | -------- | ---- | --------- |
| Custom TCP | TCP      | 3000 | 0.0.0.0/0 |
| Custom TCP | TCP      | 9090 | 0.0.0.0/0 |
| Custom TCP | TCP      | 9100 | 0.0.0.0/0 |
| SSH        | TCP      | 22   | Your IP   |

---

# Step 6: Access Monitoring Services

Replace PUBLIC_IP with your EC2 Public IP.

## Prometheus

```text
http://PUBLIC_IP:9090
```

## Grafana

```text
http://PUBLIC_IP:3000
```

Default Credentials:

```text
Username: admin
Password: admin
```

---

# Step 7: Configure Grafana Data Source

Navigate:

Connections
→ Data Sources
→ Prometheus

Prometheus URL:

```text
http://prometheus:9090
```

Click:

Save & Test

Expected:

```text
Data source is working
```

---

# Step 8: Import Grafana Dashboard

Navigate:

Dashboards
→ Import

Dashboard ID:

```text
1860
```

This imports the Node Exporter Full Dashboard.

---

# Step 9: Configure Slack Alerts

Navigate:

https://api.slack.com/apps

Create:

1. Create App
2. From Scratch
3. Select Workspace
4. Create App

Enable:

Incoming Webhooks

Add:

New Webhook to Workspace

Select Channel

Allow

Copy Webhook URL:

```text
https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX
```

---

# Step 10: Configure AIOps Settings

Navigate:

```bash
cd scripts
```

Edit:

```bash
vi config.ini
```

Update:

```ini
[monitoring]
prometheus_url = http://localhost:9090
query = 100 - avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100
slack_webhook = https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX
```

Save and Exit.

---

# Step 11: Install Python Environment

```bash
sudo dnf install python3 python3-pip -y

python3 --version
pip3 --version
```

Create virtual environment:

```bash
python3 -m venv myenv
```

Activate:

```bash
source myenv/bin/activate
```

Expected:

```text
(myenv)
```

---

# Step 12: Install Python Dependencies

Install packages:

```bash
pip install pandas
pip install requests
pip install scikit-learn
pip install joblib
pip install configparser
```

Or:

```bash
pip install -r requirements.txt
```

Verify:

```bash
pip list
```

---

# Step 13: Collect CPU Metrics

Run:

```bash
python3 fetch_metrics.py
```

Expected:

```text
CPU metrics collected successfully
```

---

# Step 14: Train Machine Learning Model

Run:

```bash
python3 train_model.py
```

Expected:

```text
Model trained successfully
```

---

# Step 15: Start Real-Time Monitoring

Run:

```bash
python3 detect_anomalies.py
```

Expected:

```text
Monitoring started...
```

---

# Step 16: Generate CPU Load

Open a new terminal session.

Install:

```bash
sudo dnf install stress-ng -y
```

Generate load:

```bash
stress-ng --cpu 2 --timeout 120s
```

For heavier testing:

```bash
stress-ng --cpu 4 --timeout 300s

stress-ng --cpu 2 --vm 2 --vm-bytes 400M --timeout 120s

```

---

# Step 17: Validate AIOps Pipeline

Verify the following:

## Grafana

* CPU spike visible
* Dashboard updates in real time

## Prometheus

* Metrics collected successfully
* Query returns CPU utilization

## Python ML Engine

* Detects abnormal CPU usage
* Prints anomaly alerts

Example:

```text
CPU Anomaly Detected
```

## Slack

* Alert message received
* Notification generated automatically

---

# Troubleshooting

## Check Running Containers

```bash
docker ps
```

## View Container Logs

```bash
docker compose logs
```

## Check Prometheus Health

```bash
curl http://localhost:9090/-/healthy
```

## Check Prometheus Targets

```bash
curl http://localhost:9090/api/v1/query?query=up
```

## Verify Open Ports

```bash
ss -tulpn | grep -E '3000|9090|9100'
```

---

# Success Criteria

The implementation is successful when:

* Prometheus is collecting EC2 metrics
* Grafana displays CPU dashboards
* Python ML model is trained
* Anomalies are detected
* Slack notifications are delivered
* CPU stress tests generate alerts
* End-to-end AIOps pipeline is operational

---

# Future Enhancements

* Memory Anomaly Detection
* Disk Usage Forecasting
* Network Traffic Analysis
* AWS CloudWatch Integration
* Capacity Planning
* Predictive Analytics
* Auto Remediation using Lambda
* Multi-Instance Monitoring
* Kubernetes Monitoring
* OpenTelemetry Integration


======================V2==========================





sudo dnf update -y

sudo dnf install git -y

git --version

git clone https://github.com/bdreddy738/aiops-mlops-devops-labs.git

cd aiops-mlops-devops-labs/DAY-01/aiops-lab

Install Docker dependencies 

sudo dnf update

sudo dnf install docker -y

sudo systemctl enable docker

sudo systemctl start docker

docker --version


mkdir -p ~/.docker/cli-plugins

curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
-o ~/.docker/cli-plugins/docker-compose

chmod +x ~/.docker/cli-plugins/docker-compose


docker compose version

systemctl status docker

sudo systemctl start docker

docker-compose up -d

docker ps

Now check Prometheus, Grafana and Slack integration

Security Group (Most Important)

Go to:

EC2
→ Instance
→ Security
→ Security Group
→ Edit Inbound Rules

Add:

Type	Port	Source
Custom TCP	3000	0.0.0.0/0
Custom TCP	9090	0.0.0.0/0
Custom TCP	9100	0.0.0.0/0

Prometheus: http://52.91.178.237:9090

Grafana: http://52.91.178.237:3000

Username: admin Password: admin

Configure Grafana Data Source
Connections → Data Sources → Prometheus

URL:

http://prometheus:9090

Save & Test

Import Dashboard
Dashboard ID: 1860

Slack Configuration
Go to:

https://api.slack.com/apps

Create App

→ From Scratch

→ Give App Name

→ Select Workspace

→ Create App

Incoming Webhooks

→ Activate Incoming Webhooks = ON

→ Add New Webhook to Workspace

→ Select Channel

→ Allow

Copy Webhook URL

Example:

https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX

Move to scripts folder
cd scripts

Change config.ini configuration
vi config.ini

Update:

prometheus_url = http://localhost:9090

slack_webhook = https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX

Install Python Virtual Environment

sudo dnf install python3 python3-pip -y
python3 --version
pip3 --version

python3 -m venv myenv

source myenv/bin/activate

Install Python Packages

pip install pandas

pip install requests scikit-learn

pip install joblib

pip install configparser

Collect CPU Metrics
python3 fetch_metrics.py

Train ML Model
python3 train_model.py

Start Real-Time Monitoring
python3 detect_anomalies.py

Open Terminal-2
sudo dnf install -y stress-ng

stress-ng --cpu 2 --timeout 120s

stress-ng --cpu 2 --vm 2 --vm-bytes 400M --timeout 120s


Compare Results
CPU utilization in Grafana Dashboard

CPU utilization in Prometheus

Slack alert messages

Terminal output showing CPU Anomaly Detected

Verify end-to-end AIOps pipeline is working successfully

===============================================


Verified Working Components
✅ EC2 Instance
✅ Node Exporter
✅ Prometheus
✅ Grafana
✅ Python Monitoring Script
✅ Isolation Forest ML Model
✅ CPU Monitoring
✅ Memory Monitoring
✅ Disk Monitoring
✅ Network Monitoring
✅ Stress Testing
✅ Anomaly Detection
✅ Slack Notifications


