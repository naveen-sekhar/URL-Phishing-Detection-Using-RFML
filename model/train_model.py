import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
def train_model():
    df = pd.read_csv("Synthetic_Dataset/phishing_dataset.csv")
    
    # Define features and target
    X = df.drop(columns=["url", "label"])
    y = df["label"]
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train = X_train.drop(columns=["safety_reason"], errors="ignore")
    X_test = X_test.drop(columns=["safety_reason"], errors="ignore")

    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save model
    joblib.dump(model, "phishing_model.pkl")
    print("✅ Model trained and saved as phishing_model.pkl")

if __name__ == "__main__":
    train_model()
