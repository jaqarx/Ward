import cv2
import numpy as np
from fer import FER

# This should work - try lowercase 'fer'
detector = FER()

HAS_PICAMERA2 = False
try:
    from picamera2 import Picamera2
    HAS_PICAMERA2 = True
except ImportError:
    pass

if HAS_PICAMERA2:
    cam = Picamera2()
    config = cam.create_preview_configuration(main={"size": (640, 480), "format": "RGB888"})
    cam.configure(config)
    cam.start()
else:
    cam = cv2.VideoCapture(0)

frame_count = 0
detection_interval = 5
last_emotion = "neutral"

try:
    while True:
        if HAS_PICAMERA2:
            frame = cam.capture_array()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        else:
            ret, frame = cam.read()
            if not ret:
                break
        
        # Detect emotion every Nth frame
        if frame_count % detection_interval == 0:
            result = detector.detect_emotions(frame)
            
            if result and len(result) > 0:
                emotions = result[0]['emotions']
                last_emotion = max(emotions, key=emotions.get)
                print(f"Emotion: {last_emotion}, Scores: {emotions}")
        
        cv2.putText(frame, f"Emotion: {last_emotion}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('Emotion Detection', frame)
        frame_count += 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cv2.destroyAllWindows()
    if HAS_PICAMERA2:
        cam.stop()
    else:
        cam.release()