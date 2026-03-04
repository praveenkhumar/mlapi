# Import FastAPI framework for building web APIs
from fastapi import FastAPI
# Import BaseModel from Pydantic for request data validation and schema definition
from pydantic import BaseModel
# Import joblib to load pre-trained machine learning models from pickle files
import joblib

# Create a FastAPI application instance that will handle HTTP requests
app = FastAPI()

# Load the pre-trained student prediction model pipeline from the saved pickle file
MODEL_VERSION = "v1"
model = joblib.load(f"models/student_pipeline_{MODEL_VERSION}.pkl")

# Define the Student data model with validation using Pydantic BaseModel
class Student(BaseModel):
    # Student marks as an integer value
    marks: int
    # Student attendance percentage as an integer value
    attendance: int

# Define a POST endpoint at "/predict" to handle prediction requests
@app.post("/predict")
# Function to predict student pass/fail status based on marks and attendance
def predict(student: Student):
    # Convert marks and attendance into a 2D array format required by scikit-learn
    # Shape: [[marks, attendance]] - one sample with two features
    data = [[student.marks, student.attendance]]

    # Get the prediction (0=Fail, 1=Pass) and extract the first (and only) result
    prediction = model.predict(data)[0]
    # Get the probability of the positive class (Pass) and extract the confidence score
    probability = model.predict_proba(data)[0][1]

    # Convert numeric prediction to readable text: 1 becomes "Pass", 0 becomes "Fail"
    result = "Pass" if prediction == 1 else "Fail"

    # Return the prediction response as a JSON object containing input data and prediction results
    return {
        # Echo back the student's marks from the request
        "marks": student.marks,
        # Echo back the student's attendance from the request
        "attendance": student.attendance,
        # Return the prediction result as a readable string ("Pass" or "Fail")
        "prediction": result,
        # Return the confidence score rounded to 2 decimal places as a float
        "confidence": round(float(probability), 2)
    }