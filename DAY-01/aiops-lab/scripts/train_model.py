# Copyright (c) 2026 CloudHired Official
# All rights reserved.

import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

def train_model():
    try:
        if not os.path.exists("cpu_metrics.csv"):
            raise FileNotFoundError(
                "cpu_metrics.csv not found - run fetch_metrics.py first"
            )

        df = pd.read_csv("cpu_metrics.csv")

        if len(df) < 10:
            raise ValueError(
                "Not enough data points (minimum 10 required)"
            )

        required_columns = [
            "cpu_usage",
            "memory_usage",
            "disk_usage",
            "network_rx",
            "network_tx"
        ]

        for col in required_columns:
            if df[col].isnull().any():
                raise ValueError(
                    f"Missing values in {col}"
                )

        features = df[
            [
                "cpu_usage",
                "memory_usage",
                "disk_usage",
                "network_rx",
                "network_tx"
            ]
        ]

        model = IsolationForest(
            contamination=0.05,
            random_state=42,
            n_estimators=100,
            max_samples='auto'
        )

        model.fit(features)

        joblib.dump(
            model,
            "aiops_model.joblib"
        )

        print(
            "✅ Model trained and saved as aiops_model.joblib"
        )

    except Exception as e:
        print(
            f"❌ Training failed: {str(e)}"
        )


if __name__ == "__main__":
    train_model()