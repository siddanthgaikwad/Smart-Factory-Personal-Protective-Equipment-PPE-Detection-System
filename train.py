from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data/ppe_dataset/data.yaml",
    epochs=10,
    imgsz=640
)