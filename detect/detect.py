from ultralytics import YOLO

model_dir = os.path.join("models", "mosquito_detection.pt")
model = YOLO(model_dir)

image_path = 'images'
output_dir = 'output'

model.predict(source=image_path, save=True, project=output_dir, name='蚊子识别结果')
