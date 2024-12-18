### README: YOLOv8 Human Head Detection

---

## Project Overview
This project involves building a **YOLOv8-based real-time object detection system** for identifying human heads using a custom dataset. The workflow includes:
1. **Dataset Creation and Labeling** using [CVAT](https://cvat.ai/).
2. **Model Training** with YOLOv8 and custom configuration.
3. **Real-Time Inference** using a webcam to detect human heads.

---

## Features
- Real-time human head detection using YOLOv8.
- Custom dataset integration with annotated labels.
- Configurable training with customizable hyperparameters.
- Compatible with webcam or video input for testing.

---

## Prerequisites
1. Python 3.8 or higher.
2. Libraries:
   - `ultralytics`
   - `opencv-python`
   - `numpy`
3. GPU support (Optional but recommended for training).

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yolov8-head-detection.git
   cd yolov8-head-detection
   ```
2. Install dependencies:
   ```bash
   pip install ultralytics opencv-python numpy
   ```
3. Set up your dataset:
   - Organize your dataset into `train` and `val` folders.
   - Annotate the data using tools like CVAT and export in YOLO format.

---

## Usage

### 1. **Training the Model**
Update `config.yaml` with the dataset paths:
```yaml
path: <your-dataset-directory>
train: images/train
val: images/val
names:
  0: head
```
Run the training script:
```bash
python main.py
```
- The model will be trained for 100 epochs (default in the script).
- Results will be saved in the `runs/detect/train/` directory.

### 2. **Testing the Model in Real-Time**
Use the trained model (`best.pt`) for real-time inference:
```bash
python test.py
```
- A webcam feed will open, displaying the detected human heads.

---

## File Structure
```
yolov8-head-detection/
├── main.py          # Script for training
├── test.py          # Script for real-time inference
├── config.yaml      # Custom dataset configuration
├── runs/            # Training results and weights
└── README.md        # Project documentation
```

---

## Troubleshooting
- **No Detection in Real-Time**:
  - Verify the `best.pt` model file is correctly loaded in `test.py`.
  - Lower the confidence threshold in `test.py`:
    ```python
    results = model.predict(source=0, conf=0.25, show=True)
    ```
- **Poor Detection Accuracy**:
  - Ensure sufficient and diverse data samples in your dataset.
  - Train for more epochs or use a larger YOLOv8 model (e.g., `yolov8m`).

---

## Future Improvements
- Extend detection to other body parts or actions.
- Integrate advanced data augmentation techniques for better generalization.
- Explore deployment on edge devices (e.g., Jetson Nano).

---

## References
- [Ultralytics YOLO Documentation](https://docs.ultralytics.com/)
- [CVAT Annotation Tool](https://cvat.ai/)
- [OpenCV Documentation](https://docs.opencv.org/)

---

## License
This project is licensed under the MIT License. See `LICENSE` for details. 

--- 

Feel free to update the content and structure as per your requirements!
