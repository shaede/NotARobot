import cv2
import time
import numpy as np
from base_camera import BaseCamera

class Camera(BaseCamera):
    @staticmethod
    def frames():
        stime = time.time()
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            ntime = time.time()
            if ( int(ntime - stime)) > 15:
                #do other opencv stuff
                #mask = cv2.inRange('hsv', low_blue, high_blue)
                #and the mask and the original image
                #edge detection
             #   edge = cv2.Canny(img, 100, 200)
                stime = time.time()
             #   yield cv2.imencode('.jpg', edge)[1].tobytes()
            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
    def filter():
        low_blue = np.array([188, 110, 255])
        high_blue = np.array([280,100,100])
        high_yellow = np.array([70, 56, 100])
        low_yellow = np.array([50, 100, 100])

        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        ret, frame = camera.read() # get a single frame
        #get color masks
        mask = cv2.inRange(frame, low_blue, high_blue)
        out = cv2.bitwise_and(frame, frame, mask = mask)
        mask = cv2.inRange(frame, low_yellow, high_yellow)
        out = cv2.bitwise_and(out, out, mask = mask)
        #draw contours around all blue and yellow objects
        out = cv2.canny(out, 100, 200)
        yield cv2.imencode('.jpg', out)[1].tobytes()



