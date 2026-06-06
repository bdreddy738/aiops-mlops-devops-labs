git clone https://github.com/bdreddy738/aiops-mlops-devops-labs.git

cd aiops-mlops-devops-labs/DAY-01/aiops-lab

# Install Docker dependencies (if not already installed)

sudo apt-get update

docker-compose up -d

# Now check Prometheus, Grafana and Slack integration

Prometheus:
http://<PUBLIC-IP>:9090

Grafana:
http://<PUBLIC-IP>:3000

Username: admin
Password: admin

# Configure Grafana Data Source

Connections
→ Data Sources
→ Prometheus

URL:

http://prometheus:9090

Save & Test

# Import Dashboard

Dashboard ID: 1860

# Slack Configuration

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

# Move to scripts folder

cd scripts

# Change config.ini configuration

vi config.ini

Update:

prometheus_url = http://localhost:9090

slack_webhook = https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX

# Install Python Virtual Environment

sudo apt install python3.12-venv -y

python3 -m venv myenv

source myenv/bin/activate

# Install Python Packages

pip install pandas

pip install requests scikit-learn

pip install joblib

pip install configparser

# Collect CPU Metrics

python3 fetch_metrics.py

# Train ML Model

python3 train_model.py

# Start Real-Time Monitoring

python3 detect_anomalies.py

# Open Terminal-2

sudo apt-get install -y stress-ng

stress-ng --cpu 2 --timeout 120s

# Compare Results

1. CPU utilization in Grafana Dashboard

2. CPU utilization in Prometheus

3. Slack alert messages

4. Terminal output showing CPU Anomaly Detected

5. Verify end-to-end AIOps pipeline is working successfully




 