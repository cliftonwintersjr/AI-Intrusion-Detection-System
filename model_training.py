print("STARTING MODEL TRAINING")

import pandas as pd # type: ignore
from sklearn.ensemble import IsolationForest # type: ignore
import joblib # type: ignore

# Load dataset
df = pd.read_csv("telecom_traffic.csv")

print(f"Dataset loaded: {df.shape}")

# Separate features (DO NOT include label for training)
features = [
    "packet_size",
    "connection_duration",
    "packets_per_second",
    "failed_connections",
    "data_transfer_rate",
    "connection_attempts"
]

X = df[features]

# Train ONLY on normal data (important concept)
normal_data = df[df["label"] == "Normal"][features]

print(f"Training on normal samples: {normal_data.shape}")

# Create model
model = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)

# Train model
model.fit(normal_data)

# Save model
joblib.dump(model, "ai_ids_model.pkl")

print("MODEL TRAINING COMPLETE")
print("Saved as ai_ids_model.pkl")