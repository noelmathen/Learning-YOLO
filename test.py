from ultralytics import YOLO

model = YOLO('yolov8n.pt')
# model = YOLO('yolo11n.pt')

results = model.predict(source='1', show=True)

print(results)