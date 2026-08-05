import cv2
import time
from adafruit_servokit import ServoKit
from time import sleep
from servoMovementServoKit import happyEars, neutralEars, sadEars, panServo, tiltServo, neutralStance
from picamera2 import Picamera2

# Ensures robot is in a known pose
neutralStance()
panAngle = 90
tiltAngle = 130

# Tuning constant
KP = 0.015

def track_face(errorX, errorY):

    # Set to global so that these variables' values are stored outside of the function
    global panAngle, tiltAngle

    # Adjusts angle slightly proportional to the error
    panAngle -= KP * errorX
    tiltAngle -= KP * errorY

    # Ensures the angles never exceed 180 degrees
    panAngle = max(0, min(180, panAngle))
    tiltAngle = max(0, min(180, tiltAngle))

    # Set the pan and tilt servos to use the adjusted angles 
    panServo.angle = panAngle
    tiltServo.angle = tiltAngle


# Tests camera livestreaming with servo angle when key is pressed
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Checks if picamera 2 library is available

# Creates instance of a camera
# Note: automatically selects first camera available (otherwise have to specify camera within parameters)
# Ex. picam2 = Picamera2(camera_num=1)
cam = Picamera2()

# Sets up camera livestream configuration (ex. color format and size of the frame)
config = cam.create_preview_configuration(main={"format": "RGB888", "size": (960, 720)})
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
            happyEars()

            # Draw rectangle around first face
            # x - x coordinate of top left corner
            # y - y coordinate of top left corner
            # w - width of rectangle
            # h - height of rectangle
            x, y, w, h = faces[0]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Face detected!", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Calculate center of rectangle around face
            centerRectX = x + (w / 2)
            centerRectY = y + (h / 2)

            # Get frame height and width
            frameHeight, frameWidth = frame.shape[:2]

            # Calculate error of center of rectangle from center of screen
            errorX = centerRectX - (frameWidth / 2)
            errorY = centerRectY - (frameHeight / 2)

            #there needs to be a direction
            # for x 
            # positive means shift to the left
            # negative means shift to the right

            # for y
            # positive means shift down
            # negative means shift up

            # Move camera towards face
            track_face(errorX, errorY)

        else:
            # No face - ears down (sad) 
            sadEars()

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
