from ultralytics import YOLO
import os

model_dir = os.path.join("models", "mosquito_detection.pt")
model = YOLO(model_dir)

image_path = 'images'

results = model(image_path)

n_mosquitoes = len(results[0].boxes)

print(f'蚊子数量: {n_mosquitoes}')
