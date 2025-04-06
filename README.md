# 🔒 Phishing URL Detector

A Machine Learning-based web application that detects whether a given URL is **legitimate** or **phishing** with detailed explanation for the same. It uses a Random Forest Classifier trained on a Synthetic dataset of 10,000 labeled URLs and provides real-time prediction through a simple, animated frontend and Flask backend.

---

## 📌 Features

- ✅ Detects phishing URLs with medium accuracy
- ⚡ Fast, real-time URL predictions with explanations
- 📊 Trained on a robust synthetic dataset with 30+ features
- 🌐 Clean, responsive UI 
- 🔁 RESTful API for backend communication
- Can be used for a custom real-time dataset
  
---

## Libraries & Other

- Python, Flask
- Scikit-learn (RandomForestClassifier)
- Pandas, Joblib
- HTML, CSS (animated), JavaScript

---

## 🗂️ Project Structure 
Refer Projectstructure.txt for Reference 

---

## 🛠️ How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/naveen-sekhar/URL-Phishing-Detection-Using-RandomForest-Machine-Learning-Model.git
   cd URL-Phishing-Detection-Using-RandomForest-Machine-Learning-Model
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
4. **(Optional) Retrain the Model**
   ```bash
   python train_model.py
6. **Run the Flask Server**
    ```bash
   python app.py
8. Open in Browser
   ```bash
   http://localhost:5000

--- 

Dataset
- File: phishing_dataset.csv
- Size: 10,000 labeled URLs
- Labels: 1 = phishing, 0 = legitimate
- Features: URL-based (e.g., length, special characters, subdomains)
- Synthetic Dataset

---
