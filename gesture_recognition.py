import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import webbrowser

# MediaPipe modules
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Path to your model
model_path = 'gesture_recognizer.task'

# Callback function to handle results
def print_result(result, output_image: mp.Image, timestamp_ms: int):
    if result.gestures:
        gesture_name = result.gestures[0][0].category_name
        # print(gesture_name)
        confidence = result.gestures[0][0].score
        print(f"Gesture: {gesture_name} ({confidence:.2f}) at {timestamp_ms} ms")

# Create recognizer options for live stream
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result
)


# Initialize camera
cap = cv2.VideoCapture(1)

# Create recognizer
with GestureRecognizer.create_from_options(options) as recognizer:
    start_time = time.time()
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Convert BGR (OpenCV) to RGB (MediaPipe)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create MediaPipe Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

        # Generate timestamp in milliseconds
        timestamp_ms = int((time.time() - start_time) * 1000)

        # Run recognition asynchronously
        recognizer.recognize_async(mp_image, timestamp_ms)

        # Display
        cv2.imshow('Gesture Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


        


