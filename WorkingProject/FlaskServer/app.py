from flask import Flask, render_template, request, Response
from camera import Camera
from keyboarded_robot import GoPiGo3WithKeyboard
from easygopigo3 import *
import sys
import gopigo3


app = Flask(__name__)
#init the servo
#servo1 = gpg.init_servo(port = "SERVO1")
@app.route('/')
def index():
    return render_template("index.html")
	
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
       # print("123")
       # buttonPress = input()
       # executeKeyboardJob(buttonPress)

def listen():
    gpg = EasyGoPiGo3()
    servo1 = gpg.init_servo(port = "SERVO1")
    while True:
        a=input()
        print(a)
        if a=='w':
           gpg.forward()
        elif a=='a':
            gpg.right()
        elif a=='d':
            gpg.left()
        elif a=='s':
            gpg.stop()
        else:
            gpg.stop()
    return 1


@app.route('/input')
def control():
    print("a")
    # while True:
    buttonPresskey = request.get.args.get('key')
    key = keyCodeBinding[buttonPressKey]
    result = gopigo3.executeKeyboardJob(buttonPressKey)

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/navigate')
def navigate():
    gpg = EasyGoPiGo3()
    servo1 = gpg.init_servo(port = "SERVO1")
    robot = gopigo3.GoPiGo3()
    while True:
        a=input()
        print(a)
        if a=='w':
            gpg.forward()
        elif a=='a':
            gpg.right()
        elif a=='d':
            gpg.left()
        elif a=='s':
            gpg.backward()
        elif a=='i':
            gpg.drive_cm(10, True)
        elif a=='j':
            gpg.backward_cm(10)
        elif a=='k':
            gpg.turn_degrees(45)
        elif a=='l':
            gpg.turn_degrees(-45)
        elif a=='f':
            robot.set_servo(robot.SERVO_1, 1850)
            #servo1.rotate_servo(-5)
            time.sleep(1)
            #servo1.rotate_servo(5)
            robot.set_servo(robot.SERVO_1,0)
        else:
            gpg.stop()
    return 1
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
    control()
