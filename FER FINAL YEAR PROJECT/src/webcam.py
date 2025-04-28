import cv2
import time

class VideoCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.prev_time = time.time()

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, 0

        # Calculate FPS
        cur_time = time.time()
        fps = int(1 / (cur_time - self.prev_time))
        self.prev_time = cur_time

        return frame, fps

    def release(self):
        self.cap.release()
