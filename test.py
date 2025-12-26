import cv2
import time
from gpiozero import AngularServo
from time import sleep
from servoMovement import servoAngle, leftEar, rightEar
from picamera2 import Picamera2

# Tests camera livestreaming with servo angle when key is pressed

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Checks if picamera 2 library is available

# Creates instance of a camera
# Note: automatically selects first camera available (otherwise have to specify camera within parameters)
# Ex. picam2 = Picamera2(camera_num=1)
cam = Picamera2()

# Sets up camera livestream configuration (ex. color format and size of the frame)
config = cam.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
cam.configure(config)
cam.start()
time.sleep(2)  # Allow camera to warm up and adjust white balance


try:
    while True:
        frame = cam.capture_array()
        # use the below for color filtering
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        
        faces = face_cascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        if len(faces) > 0:
            # Face detected - ears up!
            servoAngle(leftEar, -30)
            servoAngle(rightEar, 30)
            # Draw rectangle around first face
            x, y, w, h = faces[0]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Face detected!", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            # No face - ears down (sad)
            servoAngle(leftEar, 50)
            servoAngle(rightEar, -60)
            cv2.putText(frame, "No face", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    if HAS_PICAMERA2:
        cam.stop()
    else:
        cam.release()
    cv2.destroyAllWindows()
