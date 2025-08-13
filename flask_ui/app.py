from flask import Flask, render_template, request
import requests


app = Flask(__name__)

FASTAPI_URL = "http://localhost:8000/predict"  # Change when deployed

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Collect form data
        form_data = {
            "age": int(request.form["age"]),
            "sex": int(request.form["sex"]),
            "cp": int(request.form["cp"]),
            "trestbps": int(request.form["trestbps"]),
            "chol": int(request.form["chol"]),
            "fbs": int(request.form["fbs"]),
            "restecg": int(request.form["restecg"]),
            "thalach": int(request.form["thalach"]),
            "exang": int(request.form["exang"]),
            "oldpeak": float(request.form["oldpeak"]),
            "slope": int(request.form["slope"]),
            "ca": int(request.form["ca"]),
            "thal": int(request.form["thal"]),
        }

        # Send POST request to FastAPI
        try:
            response = requests.post(FASTAPI_URL, json=form_data)
            if response.status_code == 200:
                prediction = response.json().get("heart_disease")
            else:
                prediction = "Error: Could not get prediction"
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
