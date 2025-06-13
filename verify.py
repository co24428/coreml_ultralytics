from ultralytics import YOLO

coreml_model = YOLO("yolo11n.mlpackage")
results = coreml_model("https://ultralytics.com/images/bus.jpg")
