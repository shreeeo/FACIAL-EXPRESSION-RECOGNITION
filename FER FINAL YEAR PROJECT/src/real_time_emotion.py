import cv2
import threading
import time
from deepface import DeepFace

# Define colors for different emotions
emotion_colors = {
    "angry": (0, 0, 255),
    "disgust": (255, 0, 255),
    "fear": (255, 0, 0),
    "happy": (0, 255, 255),
    "sad": (255, 255, 0),
    "surprise": (0, 255, 0),
    "neutral": (200, 200, 200)
}

# Open webcam
cap = cv2.VideoCapture(0)

# Set video width and height for better performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Global variables
emotion = "Detecting..."
frame_lock = threading.Lock()

def analyze_emotion():
    global emotion
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            with frame_lock:
                emotion = result[0]['dominant_emotion']
        except Exception as e:
            print("Error:", e)

# Run DeepFace analysis in a separate thread to reduce lag
thread = threading.Thread(target=analyze_emotion, daemon=True)
thread.start()

prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Calculate FPS
    cur_time = time.time()
    fps = int(1 / (cur_time - prev_time))
    prev_time = cur_time

    # Display FPS
    cv2.putText(frame, f"FPS: {fps}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Display detected emotion
    with frame_lock:
        color = emotion_colors.get(emotion, (255, 255, 255))
        cv2.putText(frame, f"Emotion: {emotion.upper()}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    # Show video feed
    cv2.imshow("Real-Time Emotion Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
