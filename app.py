
from flask import Flask, render_template, request
from model import predict_message

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form.get("msg")
    result = predict_message(message)
    return render_template("index.html", result=result,score=85,
                       explanation="Contains words like 'urgent', 'click here'")

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
print("User message:", message)