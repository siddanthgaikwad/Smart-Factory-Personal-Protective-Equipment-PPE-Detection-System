# 🏭 Smart Factory PPE Detection System

An AI-powered Personal Protective Equipment (PPE) detection system built using **YOLOv8**, designed to improve workplace safety in smart factory environments. The application automatically detects PPE compliance, identifies safety violations, provides a web dashboard for monitoring, and exposes metrics for observability using Prometheus and Grafana.

---

## 📌 Overview

Industrial environments require strict adherence to safety regulations. This project leverages **Computer Vision** and **Deep Learning** to detect whether workers are wearing required PPE such as hard hats, safety vests, and masks.

The system supports:

* Image-based PPE detection
* Video-based PPE detection
* Real-time webcam monitoring
* Violation logging
* Streamlit-based dashboard
* Prometheus metrics integration
* Docker and Kubernetes deployment

---

## 🚀 Features

### 🔍 PPE Detection

* Detects safety equipment using **YOLOv8**
* Identifies:

  * Hard Hats
  * Safety Vests
  * Face Masks
  * Other PPE categories supported by the trained model

### 🎥 Multiple Detection Modes

* Image Processing
* Video Analysis
* Real-time Webcam Monitoring

### 📊 Monitoring Dashboard

* Upload images for instant PPE compliance checks
* Visualize detection results
* User-friendly Streamlit interface

### 📈 Observability

* Logs safety violations
* Prometheus metrics endpoint
* Grafana-ready monitoring support

### ☁️ Deployment Ready

* Dockerized application
* Kubernetes manifests included
* Easy cloud deployment

---

## 🛠️ Technology Stack

| Component            | Technology           |
| -------------------- | -------------------- |
| Object Detection     | YOLOv8 (Ultralytics) |
| Programming Language | Python 3.9+          |
| Dashboard            | Streamlit            |
| Monitoring           | Prometheus           |
| Visualization        | Grafana              |
| Containerization     | Docker               |
| Orchestration        | Kubernetes           |

---

## 📂 Project Structure

```text
smart_factory_ppe/
│
├── app/
│   └── dashboard.py
│
├── utils/
│   ├── detection.py
│   └── logger.py
│
├── models/
├── configs/
│
├── sample_data/
│   ├── images/
│   └── videos/
│
├── outputs/
│   └── images/
│
├── main.py
├── requirements.txt
├── Dockerfile
└── *.yaml
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository_url>
cd smart_factory_ppe
```

### Create Virtual Environment

```bash
python -m venv .venv
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### 1. Image Detection

Process all images inside a directory and save annotated results.

```bash
python main.py --mode image --input sample_data/images
```

Output images will be saved to:

```text
outputs/images/
```

---

### 2. Video Detection

Run PPE detection on a video file.

```bash
python main.py --mode video --input sample_data/videos/your_video.mp4
```

---

### 3. Webcam Detection

Run real-time PPE monitoring using your webcam.

```bash
python main.py --mode webcam
```

Press **Q** to exit.

---

## 🌐 Streamlit Dashboard

Launch the interactive dashboard:

```bash
streamlit run app/dashboard.py
```

Open:

```text
http://localhost:8501
```

Features:

* Upload images
* Detect PPE compliance
* View violation results instantly

---

## 📊 Prometheus Monitoring

The application automatically exposes metrics on:

```text
http://localhost:8000
```

These metrics can be scraped by Prometheus and visualized using Grafana dashboards.

---

## 📁 Sample Data

Add your testing files to:

### Images

```text
sample_data/images/
```

### Videos

```text
sample_data/videos/
```

---

## 🐳 Docker Deployment

Build Docker image:

```bash
docker build -t smart-factory-ppe .
```

Run container:

```bash
docker run -p 8501:8501 -p 8000:8000 smart-factory-ppe
```

---

## ☸️ Kubernetes Deployment

Apply Kubernetes manifests:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Verify deployment:

```bash
kubectl get pods
kubectl get services
```

---

## 🔒 Safety Use Cases

* Manufacturing Plants
* Smart Factories
* Construction Sites
* Warehouses
* Industrial Facilities
* Compliance Auditing

---

## 📈 Future Enhancements

* Email/SMS violation alerts
* Multi-camera support
* Employee identification integration
* Historical analytics dashboard
* Cloud deployment support
* Mobile application integration

---

## 👨💻 Author

Developed as part of a Smart Factory Safety Monitoring solution using AI-powered computer vision.

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
