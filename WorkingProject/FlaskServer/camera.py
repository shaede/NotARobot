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
    def filters():
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
        thresh = cv2.threshold(out, 127,255,0)
        bcnts = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #find the blue triangles and draw boxes
        for c in bcnts:
            if len(c) !=3:
                bcnts.remove(c)
            else:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(ret, (x,y), (x+w, y+h), (0, 255, 0), 5)
        
        #find the yellow triangles and draw xs
        mask = cv2.inRange(frame, low_yellow, high_yellow)
        out = cv2.bitwise_and(out, out, mask = mask)
        thresh = cv2.threshold(out, 127,255,0)
        ycnts = cv2.findcontours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #draw contours around all blue and yellow objects
        for y in ycnts:
            if len(y) !=3:
                ycnts.remove(y)
            else:
                x, y, w, h = cv2.boundingRect(y)
                cv2.line(ret, (x,y), (x+w,y+h), (255, 0,0),5)
                cv2.line(ret, ((x+w), (y+h)), (x, y), (255,0,0),5)

        yield cv2.imencode('.jpg', ret)[1].tobytes()



