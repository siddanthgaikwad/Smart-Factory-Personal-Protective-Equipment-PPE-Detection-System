from ultralytics import YOLO
import cv2
import numpy as np
from utils.utils import draw_violation_banner

class PPEDetector:
    def __init__(self):
        # ✅ LOAD MODELS
        self.helmet_model = YOLO("best.pt")
        self.person_model = YOLO("yolov8n.pt")

    # =========================
    # VEST DETECTION (COLOR BASED)
    # =========================
    def detect_vest(self, frame, bbox):
        x1, y1, x2, y2 = bbox

        # safety bounds
        h, w, _ = frame.shape
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)

        height = y2 - y1
        if height <= 0:
            return True

        # focus on torso region
        torso = frame[y1 + int(height * 0.3): y1 + int(height * 0.7), x1:x2]

        if torso.size == 0:
            return True  # avoid crash

        hsv = cv2.cvtColor(torso, cv2.COLOR_BGR2HSV)

        # yellow/orange vest range
        lower = np.array([10, 60, 60])
        upper = np.array([40, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)
        ratio = np.sum(mask > 0) / mask.size

        return ratio > 0.1

    # =========================
    # MAIN PROCESS FUNCTION
    # =========================
    def process_frame(self, frame):
        violations = set()
        labels_detected = set()

        # run models
        helmet_results = self.helmet_model(frame)
        person_results = self.person_model(frame)

        # =========================
        # HELMET DETECTION
        # =========================
        helmet_present = False

        for r in helmet_results:
            for box in r.boxes:
                conf = float(box.conf[0])
                if conf < 0.4:
                    continue

                cls = int(box.cls[0])
                label = self.helmet_model.names.get(cls, "unknown")
                labels_detected.add(label)

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # draw
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}",
                            (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0,255,0), 2)

                if label.lower() == "helmet":
                    helmet_present = True

        # =========================
        # PERSON + VEST DETECTION
        # =========================
        person_found = False

        for r in person_results:
            for box in r.boxes:
                conf = float(box.conf[0])
                if conf < 0.4:
                    continue

                cls = int(box.cls[0])
                label = self.person_model.names.get(cls, "unknown")

                if label == "person":
                    person_found = True

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    has_vest = self.detect_vest(frame, (x1, y1, x2, y2))

                    if not has_vest:
                        violations.add("No Vest")

                        cv2.putText(frame, "No Vest",
                                    (x1, y2 + 20),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.6, (0,0,255), 2)

        # =========================
        # HELMET VIOLATION LOGIC (FIXED)
        # =========================
        if person_found and not helmet_present:
            violations.add("No Helmet")

        # =========================
        # FINAL OUTPUT
        # =========================
        frame = draw_violation_banner(frame, list(violations))

        return frame, list(violations)