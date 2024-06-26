# this code finds a bicycle in a given url
# purpose of it is to extract the fined bicycle as a template for future template matching



import urllib.request
import torch
import numpy as np
import cv2


def display_bicycles_only(url):
    model = torch.hub.load("ultralytics/yolov5", "yolov5n", trust_repo=True)
    model.conf = 0.1
    response = urllib.request.urlopen(url)
    img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    img = image
    result = model(img)
    data_frame = result.pandas().xyxy[0]

    output_image = np.copy(image)  # Create a new image to draw on

    for index in data_frame.index:
        label = data_frame["name"][index]
        if label == "bicycle":
            x1 = int(data_frame["xmin"][index])
            y1 = int(data_frame["ymin"][index])
            x2 = int(data_frame["xmax"][index])
            y2 = int(data_frame["ymax"][index])

            conf = data_frame["confidence"][index]
            text = f"Bicycle {conf:.2f}"
            
            bicycle_roi = img[y1:y2, x1:x2]

            cv2.rectangle(output_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(
                output_image,
                text,
                (x1, y1 - 20),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (255, 0, 0),
                2,
            )
        else:
            pass


    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('image', 450, 400)
    output_image = cv2.resize(output_image, (1000, 650), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Bicycles Only", output_image)
    cv2.imshow('cropped image',bicycle_roi) 
    cv2.imwrite('template2.jpg',bicycle_roi)
    cv2.imwrite('big_image2.jpg',output_image)
    cv2.waitKey(800)


url = 'https://ep1.pinkbike.org/p6pb25906218/p6pb25906218.jpg'
display_bicycles_only(url)