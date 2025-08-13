from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model & vectorizer once at startup
with open("../model/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("../model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        email_text = request.form["email_text"]
        features = vectorizer.transform([email_text])
        pred = model.predict(features)[0]
        prediction = "Phishing" if pred == 1 else "Not Phishing"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
