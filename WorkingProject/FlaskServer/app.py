from flask import Flask, render_template, request, Response
from camera import Camera
from keyboarded_robot import GoPiGo3WithKeyboard


app = Flask(__name__)
gopigo3 =GoPiGo3WithKeyboard()
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
    control()
