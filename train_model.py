import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

# Sample dataset
data = {
    "marks": [35, 80, 50, 20, 90, 60, 30, 75],
    "attendance": [60, 90, 70, 40, 95, 80, 50, 85],
    "result": [0, 1, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["marks", "attendance"]]
y = df["result"]

# Create pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X, y)

joblib.dump(pipeline, "models/student_pipeline_v1.pkl")

print("Pipeline model saved successfully.")