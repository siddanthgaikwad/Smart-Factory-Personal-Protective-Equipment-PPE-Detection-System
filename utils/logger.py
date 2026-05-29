from datetime import datetime

class ViolationLogger:
    def log_frame(self, source_type, source_name, violations, confidences):
        with open("logs/log.csv", "a") as f:
            label = violations[0] if violations else "Safe"
            f.write(f"{datetime.now()},{source_type},{source_name},{label}\n")
