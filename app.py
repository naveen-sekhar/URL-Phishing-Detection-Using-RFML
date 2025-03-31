from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("phishing_model.pkl")

# Function to extract features from URL
def extract_features(url):
    features = {
        "length_url": len(url),
        "nb_dots": url.count('.'),
        "nb_hyphens": url.count('-'),
        "nb_slash": url.count('/'),
        "nb_qm": url.count('?'),
        "nb_eq": url.count('='),
        "nb_at": url.count('@'),
        "nb_digits": sum(c.isdigit() for c in url),
        "has_https": 1 if url.startswith("https") else 0,
        "suspect_words": 1 if any(word in url for word in ["secure", "verify", "bank", "support"]) else 0
    }
    return features

# Function to generate explanation
def get_explanation(features, prediction):
    reasons = []

    if prediction == 1:  # Model says Phishing
        if features["length_url"] > 75:
            reasons.append("The URL is unusually long, which is a common phishing tactic.")
        if features["nb_dots"] > 3:
            reasons.append("There are too many dots, which may indicate a fake subdomain.")
        if features["nb_hyphens"] > 2:
            reasons.append("Suspicious use of hyphens, often used in fake URLs.")
        if features["nb_at"] > 0:
            reasons.append("The URL contains '@', which attackers use to confuse users.")
        if features["has_https"] == 0:
            reasons.append("The URL does not use HTTPS, making it less secure.")
        if features["suspect_words"] == 1:
            reasons.append("The URL contains words like 'secure' or 'verify', often used in scams.")

        if not reasons:
            reasons.append("The model detected patterns that resemble phishing sites.")

    else:  # Model says Safe
        reasons.append("This URL does not exhibit common phishing characteristics.")

    return reasons


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get("url", "")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    features = extract_features(url)
    features_df = pd.DataFrame([features])

    prediction = model.predict(features_df)[0]
    result = "Phishing" if prediction == 1 else "Safe"

    explanation = get_explanation(features, prediction)

    return jsonify({"url": url, "prediction": result, "reasons": explanation})

if __name__ == '__main__':
    app.run(debug=True)
