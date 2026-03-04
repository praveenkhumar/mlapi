from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("student_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    marks = data.get("marks")
    attendance = data.get("attendance")

    if marks is None or attendance is None:
        return jsonify({"error": "Missing input values"}), 400

    prediction = model.predict([[marks, attendance]])[0]
    probability = model.predict_proba([[marks, attendance]])[0][1]

    result = "Pass" if prediction == 1 else "Fail"

    return jsonify({
        "marks": marks,
        "attendance": attendance,
        "prediction": result,
        "confidence": round(float(probability), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)