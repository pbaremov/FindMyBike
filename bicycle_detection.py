# # this code finds an object in an image using yolov5 algoritm
# # the purpose of this file is to look in the image, find the bicycle in it and then use 
# # the discovered object as a template for future template matching


# this code finds an object in an image using yolov5 algoritm
# the purpose of this file is to look in the image, find the bicycle in it and then use 
# the discovered object as a template for future template matching


import torch
import cv2
import urllib.request

def detect_bicycle(url):
    model = torch.hub.load("ultralytics/yolov5", "yolov5n", trust_repo=True)
    response = urllib.request.urlopen(url)
    img = cv2.imread(response)
    img = cv2.resize(img, (1000, 650))

    result = model(img)

    # print("result: ", result)

    data_frame = result.pandas().xyxy[0]

    # print("data_frame: ")
    print(data_frame)

    indexes = data_frame.index
    for index in indexes:
        label = data_frame["name"][index]
        if label == "bicycle":
            x1 = int(data_frame["xmin"][index])
            y1 = int(data_frame["ymin"][index])

            x2 = int(data_frame["xmax"][index])
            y2 = int(data_frame["ymax"][index])
            
            
            # Extract the bicycle ROI
            bicycle_roi = img[y1:y2, x1:x2]
        
            conf = data_frame["confidence"][index]
            text = label + " " + str(conf.round(decimals=2))

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(img, text, (x1, y1 - 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    # cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("image", 450, 400)
    # cv2.imshow("image", img)

    # this line will show only the slice of the picture with the bicycle. Then it could be used as a template for template matching
    cv2.imshow('cropped image',bicycle_roi) 
    cv2.waitKey()

detect_bicycle('https://ep1.pinkbike.org/p6pb25117475/p6pb25117475.jpg')








































# import torch
# import cv2


# model = torch.hub.load("ultralytics/yolov5", "yolov5n", trust_repo=True)
# img = cv2.imread("image3.jpg")
# img = cv2.resize(img, (1000, 650))

# result = model(img)

# # print("result: ", result)

# data_frame = result.pandas().xyxy[0]

# # print("data_frame: ")
# print(data_frame)

# indexes = data_frame.index
# for index in indexes:
#     label = data_frame["name"][index]
#     if label == "bicycle":
#         x1 = int(data_frame["xmin"][index])
#         y1 = int(data_frame["ymin"][index])

#         x2 = int(data_frame["xmax"][index])
#         y2 = int(data_frame["ymax"][index])
        
        
#         # Extract the bicycle ROI
#         bicycle_roi = img[y1:y2, x1:x2]
       
#         conf = data_frame["confidence"][index]
#         text = label + " " + str(conf.round(decimals=2))

#         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#         cv2.putText(img, text, (x1, y1 - 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
# cv2.namedWindow("image", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("image", 450, 400)
# cv2.imshow("image", img)

# # this line will show only the slice of the picture with the bicycle. Then it could be used as a template for template matching
# cv2.imshow('cropped image',bicycle_roi) 
# cv2.waitKey()
