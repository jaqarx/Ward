import cv2
import time
from gpiozero import AngularServo
from time import sleep
from servoBasic import servoAngle, leftEar


# Checks if picamera 2 library is available
try:
    from picamera2 import Picamera2
    HAS_PICAMERA2 = True
except Exception:
    HAS_PICAMERA2 = False

if HAS_PICAMERA2:
    # Creates instance of a camera
    # Automatically selects first camera available (otherwise have to specify camera within parameters)
    # Ex. picam2 = Picamera2(camera_num=1)
    cam = Picamera2()

    # Sets up camera livestream configuration (ex. color format and size of the frame)
    config = cam.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
    cam.configure(config)
    cam.start()
    time.sleep(2)  # Allow camera to warm up and adjust white balance
else:
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("No camera available: picamera2/libcamera missing and VideoCapture failed")
        raise SystemExit(1)

try:
    while True:
        if HAS_PICAMERA2:
            frame = cam.capture_array()
            # use the below for color filtering
            # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        else:
            ret, frame = cam.read()
            if not ret:
                print("Failed to read frame from VideoCapture")
                break

        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('u'):
            servoAngle(leftEar, 90)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    if HAS_PICAMERA2:
        cam.stop()
    else:
        cam.release()
    cv2.destroyAllWindows()
