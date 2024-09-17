from ultralytics import YOLO

def yolov8_train(epochs):
    model = YOLO("yolov8n.yaml")
    model = YOLO("yolov8n.pt")
    model = YOLO("yolov8n.yaml").load("yolov8n.pt")

    results = model.train(data="../human_data.yaml", epochs=epochs, imgsz=640)

def yolov8_detect(model, image_path):
    model = YOLO(model)
    results = model.predict(source=image_path, save=True, imgsz=640)
    return results

def yolov8_val(model):
    model = YOLO(model)
    results = model.val(data="../human_data.yaml", imgsz=640)
    return results