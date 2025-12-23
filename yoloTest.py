import cv2
from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.pt')

# Open the default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
else:
    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO model on the frame
        # The 'stream=True' argument can optimize performance for video streams
        results = model(frame, stream=True)

        # Process results and draw bounding boxes (example of how to use results)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Get coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                # Draw rectangle on frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('YOLO Face Detection', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()