from ultralytics import YOLO

model=YOLO("yolov5s.pt")

model.predict("image.jpg",show=True, save=True,conf=0.5)