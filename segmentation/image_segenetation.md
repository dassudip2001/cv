# Image Segmentation

- pip install labelme
- labelme

# Data labeling

- pip install labelme2yolo

# Train a model

yolo task=segment model=train epochs=100 data= model=yolov8m-seg.pt imgsz=640 batch-size=4
