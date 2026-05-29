import cv2

def draw_violation_banner(frame, violations):
    text = "SAFE" if not violations else "VIOLATION"
    color = (0,255,0) if not violations else (0,0,255)
    cv2.putText(frame, text, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    return frame
