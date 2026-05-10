# 🛡️ ShieldNet

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/flask-2.0+-green)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.x-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![ML](https://img.shields.io/badge/models-ML%20%2B%20DL-blueviolet)

> AI-powered network intrusion detection system — classifies DoS, DDoS, PortScan, and Brute Force attacks using Machine Learning and Deep Learning, with a Flask web interface for real-time prediction.

---

## ⚠️ Disclaimer

This project is developed for **educational and research purposes only**. It demonstrates intrusion detection concepts using the CIC-IDS2017 benchmark dataset and is not intended for production deployment without further hardening.

---

## Overview

ShieldNet is an end-to-end network intrusion detection system (NIDS) that combines classical machine learning and deep learning to classify malicious network traffic. It processes both benchmark dataset traffic and custom Wireshark-captured PCAPs — from raw packets all the way to a web-based prediction interface.

The system detects:
- **DoS** (Denial of Service)
- **DDoS** (Distributed Denial of Service)
- **PortScan** (Network Reconnaissance)
- **Brute Force** (Credential Attacks)
- **Benign** (Normal Traffic)

---

## System Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                        SHIELDNET PIPELINE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              DATA SOURCES                               │   │
│  │  CIC-IDS2017 Dataset  |  Custom PCAP (Wireshark/tshark) │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              PREPROCESSING (notebook(prep)/)            │   │
│  │  Feature extraction → Cleaning → Normalization          │   │
│  │  Feature selection → SMOTE (class imbalance)            │   │
│  │  Feature alignment (dataset ↔ custom traffic)           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              MODEL TRAINING (notebooks/)                │   │
│  │                                                         │   │
│  │  Machine Learning:        Deep Learning:                │   │
│  │  - Logistic Regression    - ANN (Artificial Neural Net) │   │
│  │  - Random Forest          - CNN (Convolutional NN)      │   │
│  │  - SVM                    - LSTM (Long Short-Term Mem)  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              MODEL SERIALIZATION (models/)              │   │
│  │  Trained models + Scaler + Label Encoder                │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              FLASK WEB APP (app.py)                     │   │
│  │  Upload traffic → Select model → Get prediction         │   │
│  │  Supports dataset input + custom PCAP input             │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Models Implemented

| Model | Type | Purpose |
|-------|------|---------|
| Logistic Regression | Machine Learning | Baseline classifier |
| Random Forest | Machine Learning | Ensemble, high accuracy |
| SVM | Machine Learning | Margin-based classification |
| ANN | Deep Learning | Feedforward neural network |
| CNN | Deep Learning | Pattern recognition in traffic features |
| LSTM | Deep Learning | Sequential/temporal traffic analysis |

---

## Dataset

- **CIC-IDS2017** — Canadian Institute for Cybersecurity benchmark dataset containing labeled network flows for DoS, DDoS, PortScan, Brute Force, and Benign traffic
- **Custom traffic** — Captured using Wireshark, processed with `tshark` for feature extraction
- **Class imbalance** — Handled using SMOTE (Synthetic Minority Oversampling Technique)
- **Feature alignment** — Ensures consistency between CIC-IDS2017 features and custom-captured traffic features

---

## Project Structure

```
ShieldNet/
│
├── app.py                    # Flask web application — prediction + interface
│
├── models/
│   └── final_dl_models/      # Trained models, scaler, label encoder
│
├── notebooks/                # Model training, EDA, experimentation
│
├── notebook(prep)/           # Data preprocessing and feature alignment
│
├── templates/                # HTML frontend templates
│
├── static/                   # CSS and UI assets
│
├── assets/                   # Images and visualizations
│
├── requirements.txt
└── .gitignore
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python, Flask |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow / Keras |
| Data Processing | Pandas, NumPy |
| Class Balancing | imbalanced-learn (SMOTE) |
| Traffic Capture | Wireshark, tshark |
| Frontend | HTML, CSS |

---

## Installation

**Clone the repository:**
```bash
git clone https://github.com/Ki1shan/ShieldNet.git
cd ShieldNet
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the application:**
```bash
python app.py
```

**Open in browser:**
```
http://127.0.0.1:5000/
```

---

## Key Concepts

- **Network Intrusion Detection (NIDS)** — passive monitoring and classification of network flows
- **CIC-IDS2017** — industry-standard benchmark dataset for IDS research
- **SMOTE** — synthetic data generation to handle severe class imbalance in attack datasets
- **Feature Engineering** — extraction of flow-level statistics from raw packet captures
- **Multi-class Classification** — simultaneous detection of multiple attack types in a single model
- **PCAP Processing** — raw packet capture → tshark → feature vector → model prediction

---

## Future Improvements

- Live network traffic capture integration
- Real-time streaming analysis
- Model optimization for higher accuracy
- Cloud deployment (AWS/GCP)
- SIEM integration (Splunk, ELK)
- API endpoint for programmatic prediction

---

## Author

**Kishan N**
Offensive Security Engineer | AI/ML Security Researcher

Built ShieldNet to bridge the gap between machine learning research and practical network security — applying deep learning techniques to real-world intrusion detection challenges.

---

## License

MIT License — see `LICENSE` file for details.

---

*Traffic doesn't lie. The model just needs to learn how to listen.*
