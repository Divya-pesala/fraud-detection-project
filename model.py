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
    ml_result = model.predict(msg_vec)[0]

    risk_score, reasons = check_risk(msg)

    # Combine ML + logic
    if ml_result == 1:
        risk_score += 30

    # Decide label
    if risk_score > 60:
        result = "Fraud"
    else:
        result = "Safe"

    explanation = ", ".join(reasons) if reasons else "No suspicious patterns"

    return result, risk_score, explanation

def check_risk(msg):
    score = 0
    reasons = []

    msg = msg.lower()

    if "otp" in msg:
        score += 30
        reasons.append("asking for OTP")

    if "urgent" in msg or "immediately" in msg:
        score += 20
        reasons.append("uses urgency")

    if "click" in msg or "link" in msg:
        score += 25
        reasons.append("contains suspicious link")

    if "account" in msg or "verify" in msg:
        score += 15
        reasons.append("requests account verification")

    return score, reasons