import urllib.request

import cv2
import numpy as np


def display_image(url):
    response = urllib.request.urlopen(url)
    img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # img.shape(250, 300, 3)
    # img.shape(1200, 700, 3)

    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("image", 250, 300)
    cv2.imshow("image", img)
    cv2.waitKey(800)
    cv2.destroyAllWindows()
    print(img.shape)
    return
