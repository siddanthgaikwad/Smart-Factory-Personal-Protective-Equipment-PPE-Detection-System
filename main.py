import argparse
# pyrefly: ignore [missing-import]
import cv2
from pathlib import Path
from utils.detection import PPEDetector
from utils.logger import ViolationLogger

def run_image_mode(detector, logger, input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    for img_file in input_path.glob("*.*"):
        frame = cv2.imread(str(img_file))
        if frame is None:
            continue

        annotated, violations = detector.process_frame(frame)
        logger.log_frame("image", img_file.name, violations, [1.0])

        save_path = output_path / img_file.name
        cv2.imwrite(str(save_path), annotated)

        print(f"{img_file.name} → {violations if violations else 'SAFE'}")

def run_video_mode(detector, logger, video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        annotated, violations = detector.process_frame(frame)
        logger.log_frame("video", video_path, violations, [1.0])

        cv2.imshow("Video Detection", annotated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def run_webcam_mode(detector, logger):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        annotated, violations = detector.process_frame(frame)
        logger.log_frame("webcam", "live", violations, [1.0])

        cv2.imshow("Webcam Detection", annotated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, choices=["image", "video", "webcam"])
    parser.add_argument("--input", help="Path to image folder or video file")
    args = parser.parse_args()

    detector = PPEDetector()
    logger = ViolationLogger()

    if args.mode == "image":
        run_image_mode(detector, logger, args.input, "outputs/images")

    elif args.mode == "video":
        run_video_mode(detector, logger, args.input)

    elif args.mode == "webcam":
        run_webcam_mode(detector, logger)

if __name__ == "__main__":
    main()
