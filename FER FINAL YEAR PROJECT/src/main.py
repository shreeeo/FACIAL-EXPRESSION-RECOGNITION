import cv2
from webcam import VideoCapture
from emotion_detector import EmotionDetector
from ui import draw_ui

# Initialize webcam and emotion detector
cap = VideoCapture()
detector = EmotionDetector()

while True:
    frame, fps = cap.get_frame()

    if frame is None:
        continue

    # Get detected emotion
    emotion = detector.get_emotion()

    # Draw UI elements
    frame = draw_ui(frame, emotion, fps)

    # Show video feed
    cv2.imshow("Real-Time Emotion Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
