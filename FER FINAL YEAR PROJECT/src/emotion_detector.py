import threading
from deepface import DeepFace

class EmotionDetector:
    def __init__(self):
        self.emotion = "Detecting..."
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self.analyze_emotion, daemon=True)
        self.thread.start()

    def analyze_emotion(self):
        from webcam import VideoCapture  # Import here to avoid circular import
        cap = VideoCapture()
        while True:
            frame, _ = cap.get_frame()
            if frame is None:
                continue

            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                with self.lock:
                    self.emotion = result[0]['dominant_emotion']
            except Exception as e:
                print("Error detecting emotion:", e)
                self.emotion = "Unknown"

    def get_emotion(self):
        with self.lock:
            return self.emotion
