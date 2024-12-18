### README for Real-Time Object Detection Script

This script demonstrates how to use the YOLO (You Only Look Once) model from the Ultralytics library for real-time object detection and tracking using a webcam.

---

#### **Setup Instructions**
1. **Install Python**  
   Ensure you have Python 3.8 or later installed on your system. You can download it from [python.org](https://www.python.org).

2. **Install the Required Libraries**  
   Install the Ultralytics library and its dependencies:
   ```bash
   pip install ultralytics
   ```

3. **Download Pretrained YOLO Weights**  
   - YOLOv8: `yolov8n.pt` (small model for fast inference).  
   - YOLOv11: `yolo11n.pt` (latest YOLO version with enhanced performance).

---

#### **Usage**
1. **Code Overview**  
   The script performs real-time inference using the webcam:
   ```python
   from ultralytics import YOLO

   model = YOLO('yolov8n.pt')  # Load YOLOv8 or YOLOv11 model
   # model = YOLO('yolo11n.pt')  # Uncomment this line to use YOLOv11 weights

   results = model.predict(source='1', show=True)  # Use '0' for default webcam
   print(results)
   ```

2. **Run the Script**  
   Save the script as `object_detection.py` and run it using:
   ```bash
   python object_detection.py
   ```

3. **Output**  
   - The webcam feed will display, with real-time bounding boxes and labels for detected objects.
   - The detection results will be printed in the terminal.

---

#### **How It Works**
1. **Load YOLO Model**  
   The `YOLO()` function initializes the model with the specified pretrained weights (`yolov8n.pt` or `yolo11n.pt`).

2. **Perform Prediction**  
   The `predict()` method processes the video stream (`source='1'`) and shows the detection results live (`show=True`).

3. **View Results**  
   The detection data, such as class labels and confidence scores, is stored in `results` and printed to the console.

---

#### **Customization**
- **Change the Video Source**: Replace `source='1'` with:
  - `'0'`: Default webcam.
  - `'<file_path>'`: Path to a video file.
- **Switch YOLO Versions**:
  - To use YOLOv11, uncomment `model = YOLO('yolo11n.pt')`.
  - Ensure you download and place the correct model weights in your working directory.
- **Fine-tune Detection Settings**: Modify parameters like `conf`, `iou`, or `max_det` in the `predict()` method.

---

#### **Dependencies**
- Python 3.8 or above
- Ultralytics library (`pip install ultralytics`)
- Webcam or video file for detection

---

#### **Notes**
- YOLOv11 provides improved accuracy and speed compared to YOLOv8 but may require more computational power.
- For GPU acceleration, ensure that your system has CUDA installed and configured.

---

#### **References**
- [Ultralytics Documentation](https://docs.ultralytics.com)
- [YOLOv8 GitHub Repository](https://github.com/ultralytics/ultralytics)

Feel free to customize the script further to suit your project needs!
