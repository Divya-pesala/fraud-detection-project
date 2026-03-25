import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("spam.csv")

X = data['message']
y = data['label']

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

def predict_message(msg):
    msg_vec = vectorizer.transform([msg])
    result = model.predict(msg_vec)[0]

    return "⚠️ Fraud Message" if result == 1 else "✅ Safe Message"

def check_risk(msg):
    score = 0
    msg = msg.lower()

    if "otp" in msg:
        score += 30
    if "urgent" in msg:
        score += 20
    if "click" in msg:
        score += 20
    if "account" in msg:
        score += 10

    return score