import pandas as pd
import joblib

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

# Load trained model
model = joblib.load("phishing_model.pkl")

if __name__ == "__main__":
    url = input("Enter a URL to check: ")
    features = extract_features(url)
    features_df = pd.DataFrame([features])
    
    prediction = model.predict(features_df)[0]
    
    explanation = []
    if features["length_url"] > 75:
        explanation.append("URL is too long.")
    if features["nb_dots"] > 3:
        explanation.append("Too many dots in the URL.")
    if features["nb_hyphens"] > 2:
        explanation.append("Suspicious use of hyphens.")
    if features["nb_at"] > 0:
        explanation.append("URL contains '@', which is uncommon for safe websites.")
    if features["has_https"] == 0:
        explanation.append("URL does not use HTTPS, which is less secure.")
    if features["suspect_words"] == 1:
        explanation.append("Contains words commonly found in phishing sites (e.g., 'verify', 'bank').")
    
    result = "🚨 The URL is **PHISHING** 🚨" if prediction == 1 else "✅ The URL is **SAFE** ✅"
    
    print(result)
    print("\nReasons:")
    for reason in explanation:
        print(f"- {reason}")
