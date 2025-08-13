from flask import Flask, render_template, request
import requests

app = Flask(__name__)
FASTAPI_URL = "http://127.0.0.1:8000/predict"  # FastAPI backend


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    form_data = {}

    if request.method == "POST":
        # Collect form data
        form_data = {k: request.form[k] for k in request.form.keys()}

        # Convert numeric values for FastAPI
        data_for_api = {}
        for k, v in form_data.items():
            try:
                if '.' in v:
                    data_for_api[k] = float(v)
                else:
                    data_for_api[k] = int(v)
            except:
                data_for_api[k] = v

        # Send POST request to FastAPI
        try:
            response = requests.post(FASTAPI_URL, json=data_for_api)
            if response.status_code == 200:
                prediction = response.json().get("heart_disease")
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction, form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)