from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)

# Keep track of the process running the detection
detection_process = None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start_detection')
def start_detection():
    global detection_process

    # Run your Python model script here
    detection_process = subprocess.Popen(["python", "C:/Users/91630/OneDrive/Desktop/Driver_Drowsiness_Website/Driver Drowsiness Detection/Drowsiness_Detection.py"])
    # No need to emit a message here

@socketio.on('stop_detection')
def stop_detection():
    global detection_process

    # Stop the detection process
    if detection_process is not None:
        detection_process.terminate()
        # No need to emit a message here

if __name__ == '__main__':
    socketio.run(app, debug=True)

##  changed audio
