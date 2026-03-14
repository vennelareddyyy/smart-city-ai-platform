Smart City AI Platform

An AI-powered decision support platform for traffic congestion prediction and smart city monitoring.

This system provides an interactive dashboard that predicts traffic congestion using machine learning, visualizes traffic analytics, and displays monitoring locations on an interactive city map.

Dashboard Preview

Features

AI-based Traffic Congestion Prediction

Interactive Smart City Dashboard

Traffic Analytics Visualization using charts

City Traffic Monitoring Map using Leaflet

Machine Learning model for congestion forecasting

Tech Stack
Frontend

HTML

CSS

JavaScript

Chart.js

Leaflet.js

Backend

Python

Flask

Machine Learning

Scikit-Learn

Linear Regression

Project Architecture
Frontend Dashboard
        ↓
Flask Backend API
        ↓
Machine Learning Model
        ↓
Traffic Dataset
Project Structure
smart-city-ai-platform
│
├── backend
│     └── app.py
│
├── frontend
│     ├── index.html
│     └── app.js
│
├── models
│     ├── train_model.py
│     └── traffic_model.pkl
│
├── data
│     └── traffic_data.csv
│
├── images
│     └── dashboard.png
│
├── docs
│
└── README.md
How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/vennelareddyyy/smart-city-ai-platform.git
2️⃣ Install dependencies
pip install flask pandas scikit-learn
3️⃣ Train the machine learning model
python models/train_model.py
4️⃣ Start the backend server
python backend/app.py

The server will start at:

http://127.0.0.1:5000
5️⃣ Open the dashboard

Open this file in your browser:

frontend/index.html
Future Improvements

Real-time traffic data integration

LSTM-based deep learning traffic forecasting

Waste classification using computer vision

Integration with IoT-based smart city sensors

Deployment using Docker / Cloud platforms

Author

Vennela Reddy
MS Computer Science – Data Science
University of North Carolina at Charlotte

License

This project is developed for educational and research purposes.