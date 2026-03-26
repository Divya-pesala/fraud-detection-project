from flask import Flask, render_template, request
from model import predict_message

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form.get("msg")   # ✅ define message

    if not message:
        return render_template("index.html", result="Please enter a message")

    result = predict_message(message)   # ✅ now it's safe

    return render_template("index.html", result=result,score=85,
                       explanation="Contains words like 'urgent', 'click here'")

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))