from ultralytics import YOLO


model = YOLO('F:\code/Lions_track/runs/detect/train3/weights/best.pt')

result = model.train(data='config.yaml', epochs=10)

model.export(format='onnx')