from ultralytics import YOLO

model = YOLO('./best.pt')  



model.predict(source='./Butterflies Flying in Slow Motion HD - Houston Butterfly Museum.mp4',save=True,show=True,show_labels=True,show_conf=True,conf=0.5,save_txt=False)  # predict images in data/images/ and save to output/


