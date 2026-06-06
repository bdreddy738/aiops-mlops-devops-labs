# Copyright (c) 2026 CloudHired Official
# All rights reserved.

import joblib
import requests
import time
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

MODEL_FILE = "aiops_model.joblib"

PROM_URL = config['monitoring']['prometheus_url']

CPU_QUERY = config['monitoring']['cpu_query']
MEMORY_QUERY = config['monitoring']['memory_query']
DISK_QUERY = config['monitoring']['disk_query']
NETWORK_RX_QUERY = config['monitoring']['network_rx_query']
NETWORK_TX_QUERY = config['monitoring']['network_tx_query']

SLACK_WEBHOOK = config['monitoring']['slack_webhook']


def get_metric(query):
    try:
        response = requests.get(
            f"{PROM_URL}/api/v1/query",
            params={"query": query},
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

        return float(
            data["data"]["result"][0]["value"][1]
        )

    except Exception as e:
        print(f"⚠️ Fetch error: {str(e)}")
        return None


def alert_slack(message):
    try:
        requests.post(
            SLACK_WEBHOOK,
            json={"text": message},
            timeout=5
        )

        print("✅ Slack alert sent")

    except Exception as e:
        print(f"⚠️ Slack alert failed: {str(e)}")


if __name__ == "__main__":

    if not os.path.exists(MODEL_FILE):
        exit(
            "❌ Model file not found - run train_model.py first"
        )

    if not os.path.exists('config.ini'):
        exit("❌ config.ini not found")

    if SLACK_WEBHOOK == "YOUR_SLACK_WEBHOOK_URL":
        print(
            "⚠️ Warning: Please configure Slack webhook in config.ini"
        )

    model = joblib.load(MODEL_FILE)

    print(
        "✅ AIOps detector started. Monitoring Infrastructure..."
    )

    while True:

        cpu = get_metric(CPU_QUERY)
        memory = get_metric(MEMORY_QUERY)
        disk = get_metric(DISK_QUERY)
        network_rx = get_metric(NETWORK_RX_QUERY)
        network_tx = get_metric(NETWORK_TX_QUERY)

        if None not in [
            cpu,
            memory,
            disk,
            network_rx,
            network_tx
        ]:

            pred = model.predict(
                [[
                    cpu,
                    memory,
                    disk,
                    network_rx,
                    network_tx
                ]]
            )

            if pred[0] == -1:

                msg = f"""
🚨 Infrastructure Anomaly Detected

CPU Usage      : {cpu:.2f}%
Memory Usage   : {memory:.2f}%
Disk Usage     : {disk:.2f}%
Network RX     : {network_rx:.2f}
Network TX     : {network_tx:.2f}
"""

                print(msg)

                alert_slack(msg)

            else:

                print(
                    f"✅ Normal | "
                    f"CPU={cpu:.2f}% | "
                    f"Memory={memory:.2f}% | "
                    f"Disk={disk:.2f}%"
                )

        time.sleep(30)