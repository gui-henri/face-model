import cv2
import sys

class WebCam:
    def __init__(self, webcam_index=0):
        self.cap = cv2.VideoCapture(webcam_index)
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            sys.exit(1)

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Failed to capture image")
            sys.exit(1)
        return frame
    
    def convert_frame_rgb(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()