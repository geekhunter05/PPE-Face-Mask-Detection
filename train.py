from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data=r"C:\Users\Lenovo\Downloads\lab.py\Corona-2\data.yaml",
    epochs=75,
    imgsz=640,
    batch=16,
    project="runs/train",
    name="mask_detection_75"
)