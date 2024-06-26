from ultralytics import YOLO


model = YOLO("yolov8n.yaml")
model.train(
    data="C:/Users/Petko/Documents/University/Final Project/SoftwareEvidence/bike_detector.v1i.yolov8/data.yaml",
    epochs=35,
    batch=8,
)
model.val()
# success = model.export(format='onnx')

# from roboflow import Roboflow

# rf = Roboflow(api_key="q46vvAvjgrsSYY732pD2")
# project = rf.workspace().project("bike_detector-ki6j2")
# model = project.version(1).model

# # infer on a local image
# model.predict(
#     r"C:\Users\Petko\Documents\University\Final Project\SoftwareEvidence\2021-carrera-subway-all-weather-edition-mens-hybrid-bike-full-1.jpg",
#     confidence=40,
#     overlap=30,
# ).save('predictions.jpg')

# # visualize your prediction
# # model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# # infer on an image hosted elsewhere
# # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30)
