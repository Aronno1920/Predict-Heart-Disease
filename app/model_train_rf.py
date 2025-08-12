import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# 1. Load dataset
df = pd.read_csv("sample_data/heart.csv")

# 2. Separate features & target
X = df.drop("target", axis=1)
y = df["target"]

# 3. Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create and train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42
)
model.fit(X_train, y_train)

# 5. Evaluate model (optional, just to check)
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# 6. Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/heart_model.joblib")

print("Model saved to model/heart_model.joblib")