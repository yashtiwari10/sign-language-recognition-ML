# ✋ Sign Language Recognition using Machine Learning

This is my personal Machine Learning project where I built a real-time **Sign Language Recognition System** using **OpenCV**, **TensorFlow Lite**, and a custom-trained classifier.  
The model recognizes three hand signs: **Thumbs Up**, **OK**, and **Victory (V) Sign** using live webcam input.

This project is designed, developed, and tested entirely by me.

---

## 🚀 What This Project Does

- Opens the webcam and captures a live video stream  
- Identifies the Region of Interest (hand area)  
- Extracts features and classifies gestures  
- Displays the predicted gesture in real-time  
- Contains scripts for:
  - Creating the dataset  
  - Training the model  
  - Running real-time inference  

---

## 📂 My Project Structure

sign-language-recognition-ML/
│
├── frontend/ # UI-related code (if applicable)
│
├── backend/
│ ├── create_dataset.py # Captures dataset images (100 per class)
│ ├── train_classifier.py # Trains the ML model
│ ├── inference_classifier.py # Runs real-time gesture prediction
│ ├── model.tflite # Final trained model
│ ├── label_map.txt # Class labels
│
├── data/ # Automatically generated dataset
│ ├── 0/ # Class 0 images
│ ├── 1/ # Class 1 images
│ ├── 2/ # Class 2 images
│
└── README.md


---

## 🧠 How I Built It

### **1. Dataset Creation**
I wrote a Python script that uses OpenCV to:
- Open the webcam  
- Wait for me to press **Q**  
- Capture 100 images for each class  
- Store them in separate folders under `/data`

Command:
```bash
python backend/create_dataset.py
Model Training
I trained a gesture classifier using a lightweight TensorFlow model.
Command:
python backend/train_classifier.py
After training, the script:
Generates model.tflite
Saves accuracy results
Creates/updates label_map.txt
Real-Time Prediction
To test the model in real-time:
python backend/inference_classifier.py
This opens the webcam and shows the predicted sign on the screen.
🛠 Technologies I Used
Python 3.10
OpenCV (for real-time camera processing)
TensorFlow Lite (for efficient model inference)
NumPy
Scikit-learn

✨ Features I Implemented
Real-time gesture detection
3-class classification (Thumbs Up, OK, Victory)
Custom dataset generation
Lightweight, fast model inference
Clean backend folder structure
🎯 What I Want to Improve Next
These are the improvements I plan to add:
More gesture classes
Switch from contour detection → Mediapipe
Use a CNN-based model
Build a Streamlit web app for deployment
Host the project for public use
📌 My Motivation
I built this project to:
Learn about ML pipelines
Understand real-time computer vision
Develop a complete end-to-end ML project
Add a strong project to my GitHub portfolio

⭐ If you liked this project :
Please give it a star (⭐) on GitHub — it motivates me to continue building amazing projects!
