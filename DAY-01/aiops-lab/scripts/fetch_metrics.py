# Copyright (c) 2026 CloudHired Official
# All rights reserved.

import requests
import pandas as pd
import time
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

PROM_URL = config['monitoring']['prometheus_url']

CPU_QUERY = config['monitoring']['cpu_query']
MEMORY_QUERY = config['monitoring']['memory_query']
DISK_QUERY = config['monitoring']['disk_query']
NETWORK_RX_QUERY = config['monitoring']['network_rx_query']
NETWORK_TX_QUERY = config['monitoring']['network_tx_query']


def get_metric_history(query, start, end):
    response = requests.get(
        f"{PROM_URL}/api/v1/query_range",
        params={
            "query": query,
            "start": start,
            "end": end,
            "step": "60s"
        },
        timeout=10
    )

    response.raise_for_status()
    return response.json()


def fetch_historical(hours=1):
    try:
        if not os.path.exists('config.ini'):
            raise FileNotFoundError("config.ini not found")

        end = int(time.time())
        start = end - hours * 3600

        cpu_data = get_metric_history(CPU_QUERY, start, end)
        memory_data = get_metric_history(MEMORY_QUERY, start, end)
        disk_data = get_metric_history(DISK_QUERY, start, end)
        rx_data = get_metric_history(NETWORK_RX_QUERY, start, end)
        tx_data = get_metric_history(NETWORK_TX_QUERY, start, end)

        print(f"CPU Results    : {len(cpu_data['data']['result'])}")
        print(f"Memory Results : {len(memory_data['data']['result'])}")
        print(f"Disk Results   : {len(disk_data['data']['result'])}")
        print(f"RX Results     : {len(rx_data['data']['result'])}")
        print(f"TX Results     : {len(tx_data['data']['result'])}")

        if not cpu_data["data"]["result"]:
            raise ValueError("CPU query returned no data")

        if not memory_data["data"]["result"]:
            raise ValueError("Memory query returned no data")

        if not disk_data["data"]["result"]:
            raise ValueError("Disk query returned no data")

        if not rx_data["data"]["result"]:
            raise ValueError("Network RX query returned no data")

        if not tx_data["data"]["result"]:
            raise ValueError("Network TX query returned no data")

        cpu_points = cpu_data["data"]["result"][0]["values"]
        memory_points = memory_data["data"]["result"][0]["values"]
        disk_points = disk_data["data"]["result"][0]["values"]
        rx_points = rx_data["data"]["result"][0]["values"]
        tx_points = tx_data["data"]["result"][0]["values"]

        min_len = min(
            len(cpu_points),
            len(memory_points),
            len(disk_points),
            len(rx_points),
            len(tx_points)
        )

        df = pd.DataFrame()

        df["timestamp"] = [cpu_points[i][0] for i in range(min_len)]

        df["cpu_usage"] = [float(cpu_points[i][1]) for i in range(min_len)]
        df["memory_usage"] = [float(memory_points[i][1]) for i in range(min_len)]
        df["disk_usage"] = [float(disk_points[i][1]) for i in range(min_len)]
        df["network_rx"] = [float(rx_points[i][1]) for i in range(min_len)]
        df["network_tx"] = [float(tx_points[i][1]) for i in range(min_len)]

        df.to_csv("cpu_metrics.csv", index=False)

        print(f"✅ Saved {len(df)} metrics to cpu_metrics.csv")

    except requests.exceptions.RequestException as e:
        print(f"❌ Network Error: {str(e)}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    fetch_historical(hours=6)