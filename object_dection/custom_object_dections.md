# Create virtual environment and activate it

- python3 -m venv myenv
- source myenv/bin/activate

# Download images from the internet

- pip install simple_image_download==0.4
- run download_images_from_interent.py

# Annotate the images with the labelImg tool

- LabelImg is a graphical image annotation tool.
- pip install labelImg

# Run the labelImg tool

- labelImg

# Setup YoloV8

- pip install ultralytics
-

# Train Custom Object Detection Model

- yolo task=detect model=train epochs=100 data=custom_data.yaml model=yolov8m.pt imgsz=640 batch-size=16

# Prediction on images, videos, and webcam

- run app.py
