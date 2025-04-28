import cv2

# Define colors for different emotions
EMOTION_COLORS = {
    "angry": (0, 0, 255),
    "disgust": (255, 0, 255),
    "fear": (255, 0, 0),
    "happy": (0, 255, 255),
    "sad": (255, 255, 0),
    "surprise": (0, 255, 0),
    "neutral": (200, 200, 200),
    "unknown": (255, 255, 255)
}

def draw_ui(frame, emotion, fps):
    # Display FPS
    cv2.putText(frame, f"FPS: {fps}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Get color for detected emotion
    color = EMOTION_COLORS.get(emotion, (255, 255, 255))

    # Display emotion text
    cv2.putText(frame, f"Emotion: {emotion.upper()}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    return frame
