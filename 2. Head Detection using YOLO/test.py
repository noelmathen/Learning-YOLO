from ultralytics import YOLO

model = YOLO("2. Head Detection using YOLO/runs/detect/train/weights/best.pt")

results = model.predict(source=1, conf=0.5, show=True)
