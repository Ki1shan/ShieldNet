# ShieldNet – AI-Based Cybersecurity Threat Monitoring System

ShieldNet is an intrusion detection system designed to analyze network traffic and classify cyber attacks using machine learning and deep learning techniques. The system processes both benchmark datasets and custom captured traffic to identify threats such as DoS, DDoS, PortScan, and Brute Force attacks.

## Project Overview

This project focuses on building an end-to-end pipeline for detecting malicious network activity. It combines data preprocessing, feature engineering, model training, and deployment into a single system with a user-friendly web interface.

## Key Features
Multi-class attack detection (DoS, DDoS, PortScan, Brute Force, Benign)

Data preprocessing including cleaning, normalization, and feature selection

Class imbalance handling using SMOTE

Implementation of multiple models:

  1. Machine Learning (Logistic Regression, Random Forest, SVM)

  2. Deep Learning (ANN, CNN, LSTM)

Real-time prediction using a Flask web application

Support for both dataset-based and custom network traffic inputs

## Dataset
CIC-IDS2017 dataset used for training and evaluation

Custom network traffic captured using Wireshark and processed with tshark

Feature alignment performed to ensure consistency between training and prediction data

## System Pipeline

Raw Network Traffic (PCAP / Dataset):

→ Feature Extraction (tshark / dataset processing)

→ Data Preprocessing (cleaning, normalization, feature selection)

→ Model Training (ML & DL models)

→ Model Serialization (scaler, encoder, trained model)

→ Flask Application (prediction + interface)

## Tech Stack
Python

Flask

Scikit-learn

TensorFlow / Keras

Pandas, NumPy

Wireshark & tshark

## Project Structure

app.py – Main Flask application for prediction and interface

models/ – Trained models, scaler, and label encoder

notebooks/ – Model training, EDA, and experimentation

notebook(prep)/ – Data preprocessing and feature alignment

templates/ – HTML files for frontend

static/ – CSS and UI assets

assets/ – Images and visualizations

## How to Run
1. Clone the repository
```
git clone https://github.com/Ki1shan/ShieldNet
```

2. Navigate to the project folder
```
cd ShieldNet
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the application
```
python app.py
```
5. Open in browser
```
http://127.0.0.1:5000/
```

## Future Improvements

Integration with live network traffic capture

Real-time streaming analysis

Model optimization for higher accuracy

Deployment on cloud platforms

Integration with SIEM tools

## Disclaimer

This project is developed for educational purposes. It demonstrates intrusion detection concepts and is not intended for production deployment.
