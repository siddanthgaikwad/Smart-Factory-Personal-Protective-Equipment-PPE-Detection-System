import cv2
import streamlit as st
import numpy as np
from PIL import Image
import sys
import os

# =========================
# IMPORT DETECTOR
# =========================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.detection import PPEDetector

# =========================
# UI
# =========================
st.title("🦺 Smart Factory PPE Detection")

# =========================
# PROMETHEUS (FINAL FIX)
# =========================
from prometheus_client import Counter, start_http_server, REGISTRY

def get_or_create_counter(name, description):
    if name in REGISTRY._names_to_collectors:
        return REGISTRY._names_to_collectors[name]
    return Counter(name, description)

REQUEST_COUNT = get_or_create_counter(
    'app_requests_total', 'Total number of requests'
)

VIOLATION_COUNT = get_or_create_counter(
    'violations_total', 'Total violations detected'
)

# START SERVER ONLY ONCE
if "metrics_started" not in st.session_state:
    start_http_server(8000)
    st.session_state.metrics_started = True

# =========================
# LOAD MODEL (ONLY ONCE)
# =========================
@st.cache_resource
def load_model():
    return PPEDetector()

detector = load_model()

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    REQUEST_COUNT.inc()

    image = Image.open(uploaded_file).convert("RGB")
    frame = np.array(image)

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    frame, violations = detector.process_frame(frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    st.image(frame, width=700)

    if violations:
        VIOLATION_COUNT.inc()
        st.error(f"⚠️ Violations: {violations}")
    else:
        st.success("✅ Safe")