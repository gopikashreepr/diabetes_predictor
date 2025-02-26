# diabetes_predictor

# Diabetes Prediction Model  
A machine learning-based API that predicts diabetes using a deep learning model trained on medical data.  

## 🚀 Features  
- Predicts diabetes based on input parameters.  
- Uses a **Feedforward Neural Network (FNN)** model.  
- Flask API for easy integration.  
- StandardScaler for data preprocessing.  

## 📂 Project Structure
- 📁 diabetes-predictor
- - ┣ 📜 app.py # Flask API
- - ┣ 📜 model.py # Model Training
- - ┣ 📜 diabetes_model.h5 # Trained Model
- - ┣ 📜 scaler.pkl # Saved Scaler
- - ┣ 📜 requirements.txt # Dependencies
- - ┣ 📜 README.md # Project Documentation

## ⚙️ Installation & Setup  
1️⃣ **Clone the repository:**  
```sh
git clone https://github.com/gopikashreepr/diabetes-predictor.git
cd diabetes-predictor
```
2️⃣ **Install dependencies:**

```sh
pip install -r requirements.txt
```

3️⃣ Run the Flask API:

```sh
python app.py
```

## 🛠 Technologies Used
- Python
- TensorFlow/Keras (Deep Learning)
- Flask (API Development)
- scikit-learn (Preprocessing & Scaling)
