# 🔒 Phishing URL Detector

A Machine Learning-based web application that detects whether a given URL is **legitimate** or **phishing**. It uses a Random Forest Classifier trained on a Synthetic dataset of 10,000 labeled URLs and provides real-time prediction through a simple, animated frontend and Flask backend.

---

## 📌 Features

- ✅ Detects phishing URLs with medium accuracy
- ⚡ Fast, real-time URL predictions
- 📊 Trained on a robust synthetic dataset with 30+ features
- 🌐 Clean, responsive UI with modern animations
- 🔁 RESTful API for backend communication
- Can be use for a custom real-time dataset
  
---

## 🧠 Technologies Used

- Python, Flask
- Scikit-learn (RandomForestClassifier)
- Pandas, Joblib
- HTML, CSS (animated), JavaScript

---

## 🗂️ Project Structure 
phishing-url-detector/ │ ├── app.py # Flask backend for serving predictions ├── train_model.py # Trains ML model and saves it to .pkl ├── predict_model.py # Extracts features and predicts ├── phishing_model.pkl # Pre-trained Random Forest model ├── phishing_dataset.csv # Dataset with labeled URLs │ ├── templates/ │ └── index.html # Frontend HTML form │ ├── static/ │ ├── style.css # Stylish UI with modern design │ └── script.js # Sends request & displays result

---

## 🛠️ How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/phishing-url-detector.git
   cd phishing-url-detector
2. **Install Dependencies**
   pip install -r requirements.txt
3. **(Optional) Retrain the Model**
   python train_model.py
4. **Run the Flask Server**
   python app.py
5. Open in Browser
   http://localhost:5000

--- 

Dataset
File: phishing_dataset.csv
Size: 10,000 labeled URLs
Labels: 1 = phishing, 0 = legitimate
Features: URL-based (e.g., length, special characters, subdomains)
Synthetic Dataset

---
