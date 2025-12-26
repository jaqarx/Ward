import cv2
from ultralytics import YOLO
from picamera2 import Picamera2

# Load the model
model = YOLO('yolov11n-face.pt')

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
    config = cam.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
    cam.configure(config)
    cam.start()
else:
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("No camera available: picamera2/libcamera missing and VideoCapture failed")
        raise SystemExit(1)

frame_count = 0
detection_interval = 5

try:
    while True:
        if HAS_PICAMERA2:
            # Read a frame from the video capture
            frame = cam.capture_array()

            # Run YOLO model on the frame
            # The 'stream=True' argument can optimize performance for video streams

            if frame_count % detection_interval == 0:
                results = model(frame, stream=True, verbose=False) # what is verbose
                
                last_boxes = []
            # Process results and draw bounding boxes (example of how to use results)
                for result in results:
                    boxes = result.boxes
                    for box in boxes:
                        # Get coordinates
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        last_boxes.append((x1, y1, x2, y2))
                        

            # Display the frame
            for (x1, y1, x2, y2) in last_boxes:
                # Draw rectangle on frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            cv2.imshow('YOLO Face Detection', frame)
            frame_count += 1

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Release the capture and destroy windows
finally:
    if HAS_PICAMERA2:
        cam.stop()
    else:
        cam.release()
    cv2.destroyAllWindows()
