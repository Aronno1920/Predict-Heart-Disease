import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib
import os


# 1. Load dataset from sample_data
df = pd.read_csv("sample_data/heart.csv")

# 2. Separate features & target
X = df.drop("target", axis=1)
y = df["target"]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create pipeline with standardization + Random Forest
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("rf", RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ))
])

# 5. Train model
pipeline.fit(X_train, y_train)

# 6. Evaluate accuracy
accuracy = pipeline.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# 7. Save model
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/heart_model.joblib")

print("Model saved to model/heart_model.joblib")