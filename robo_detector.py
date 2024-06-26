# this file contains a function
# that will make a predicition on a given image using the
# roboflow detector


from roboflow import Roboflow

rf = Roboflow(api_key="q46vvAvjgrsSYY732pD2")
project = rf.workspace().project("bike_detector-ki6j2")
model = project.version(1).model

# infer on a local image
def robo_detector(url):
    model.predict(
        url, hosted=True
        # confidence,
        # overlap,
    )







# import torch
# from ultralytics import YOLO
# from PIL import Image
# import matplotlib.pyplot as plt

# # Step 1: Load the YOLOv8 model
# model_path = 'C:/Users/Petko\Documents/University/Final Project/SoftwareEvidence/bike_detector.v1i.yolov8/best.pt'  # Replace with the path to your model
# model = YOLO(model_path)

# # Step 2: Load an image
# image_path = 'C:/Users/Petko\Documents/University/Final Project/SoftwareEvidence/bike_detector.v1i.yolov8/train/images/IMG_20240605_085135_1_jpg.rf.170b97e6b01a6e0812b3c64238f01b06.jpg'


# # Replace with the path to your image C:\Users\Petko\Document
# image = Image.open(image_path)

# # Step 3: Make predictions
# results = model.predict(image)

# # Step 4: Process and visualize the results
# # Assuming results[0] contains the predicted results for the first image
# boxes = results[0].boxes  # Extract boxes

# # Visualize the results
# fig, ax = plt.subplots(1, 1, figsize=(12, 9))
# ax.imshow(image)

# # Draw the bounding boxes on the image
# for box in boxes:
#     x1, y1, x2, y2 = box.xyxy  # Get bounding box coordinates
#     conf = box.conf  # Confidence score
#     cls = box.cls  # Class label

#     rect = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, color='red', linewidth=2)
#     ax.add_patch(rect)
#     plt.text(x1, y1, f'{cls} {conf:.2f}', bbox=dict(facecolor='yellow', alpha=0.5), fontsize=12, color='black')

# plt.show()

# # import torch
# from ultralytics import YOLO
# from PIL import Image
# import matplotlib.pyplot as plt

# # Step 1: Load the YOLOv8 model
# model_path = r'C:/Users/Petko/Documents/University/Final Project/SoftwareEvidence/bike_detector.v1i.yolov8/best.pt'  # Use raw string for path
# model = YOLO(model_path)


# # Step 2: Load an image
# image_path = r'C:\Users\Petko\Downloads\WhatsApp-Image-2020-04-15-at-20.12.09.jpeg'  # Use raw string for path
# image = Image.open(image_path)

# # Step 3: Make predictions
# results = model.predict(image,conf=0.25)
# threshold = 0.5
# # Step 4: Process and visualize the results
# # Assuming results[0] contains the predicted results for the first image
# boxes = results[0].boxes  # Extract boxes

# # Visualize the results
# fig, ax = plt.subplots(1, 1, figsize=(12, 9))
# ax.imshow(image)

# # Draw the bounding boxes on the image
# for box in boxes:
#     x1, y1, x2, y2 = box.xyxy.numpy()  # Convert to numpy array if necessary
#     conf = box.conf.item()  # Convert to Python float
#     cls = int(box.cls.item())  # Convert to integer class label

#     rect = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, color='red', linewidth=2)
#     ax.add_patch(rect)
#     plt.text(x1, y1, f'{cls} {conf:.2f}', bbox=dict(facecolor='yellow', alpha=0.5), fontsize=12, color='black')

# plt.show()


# import torch
# from ultralytics import YOLO
# from PIL import Image
# import matplotlib.pyplot as plt

# # Step 1: Load the YOLOv8 model
# model_path = r'C:/Users/Petko/Documents/University/Final Project/SoftwareEvidence/bike_detector.v1i.yolov8/best.pt'
# model = YOLO(model_path)

# # Step 2: Load an image
# image_path = r'C:/Users/Petko/Documents/University/Final Project/SoftwareEvidence/bike_detector.v1i.yolov8/train/images/IMG_20240605_085135_1_jpg.rf.170b97e6b01a6e0812b3c64238f01b06.jpg'
# image = Image.open(image_path)

# # Step 3: Make predictions
# # Adjust the confidence threshold to a lower value if necessary
# results = model.predict(image, conf=0.11)  # Set conf threshold to 0.25 for more detections

# # Debugging: Check if any detections are made
# if len(results[0].boxes) == 0:
#     print("No detections were made. Please check the following:")
#     print("1. Model training quality and data diversity.")
#     print("2. Correctness of model path and file.")
#     print("3. Image preprocessing steps.")
#     print("4. Confidence threshold value.")
# else:
#     # Step 4: Process and visualize the results
#     boxes = results[0].boxes  # Extract boxes

#     # Visualize the results
#     fig, ax = plt.subplots(1, 1, figsize=(12, 9))
#     ax.imshow(image)

#     # Draw the bounding boxes on the image
#     for box in boxes:
#         x1, y1, x2, y2 = box.xyxy.numpy()  # Convert to numpy array if necessary
#         conf = box.conf.item()  # Convert to Python float
#         cls = int(box.cls.item())  # Convert to integer class label

#         rect = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, color='red', linewidth=2)
#         ax.add_patch(rect)
#         plt.text(x1, y1, f'{cls} {conf:.2f}', bbox=dict(facecolor='yellow', alpha=0.5), fontsize=12, color='black')

#     plt.show()

# from ultralytics import YOLO


# model_path = r"C:\Users\Petko\runs\detect\train7\weights\best.pt"
# model = YOLO(model_path)


# model.predict(
#     r"C:\Users\Petko\Documents\University\Final Project\SoftwareEvidence\bike_detector.v1i.yolov8\train\images\IMG_20240605_085108_jpg.rf.7badc4f1f5804df1caaf49c0c55c5d3c.jpg",
# )





# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30)
