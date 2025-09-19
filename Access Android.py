import urllib.request
import cv2
import numpy as np

# Replace with your phone's IP Webcam URL
URL = "http://192.168.1.3:8080/shot.jpg"  # Change this!

while True:
    # Fetch image from the phone camera
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
    
    # Decode the image to OpenCV format
    img = cv2.imdecode(img_arr, -1)
    
    # Show the image in a window
    cv2.imshow('IP Webcam Feed', img)
    
    # Press any key to exit
    if cv2.waitKey(1) == 27:  # ESC key
        break

cv2.destroyAllWindows()
