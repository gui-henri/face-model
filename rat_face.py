from face_detection import FaceLandmarkDetection
from model import Model3D
from rotation import SmoothRotation
from webcam import WebCam

class RatFace:
    def __init__(self, webcam: WebCam, face_detection: FaceLandmarkDetection):
        self.model = Model3D((0, 0, 0), 
                        model_path="data/model/listicon.obj", 
                        texture_path="data/model/listicon.png",
                        scale=1,
                        color=(255, 255, 255, 255)
                    )
        self.__face_detection = face_detection
        self.__webcam = webcam
        self.__rotator = SmoothRotation()

    def update(self):
        frame = self.__webcam.read()
        rgb_frame = self.__webcam.convert_frame_rgb(frame)
        face = self.__face_detection.process(rgb_frame)
        if face:
            angle = self.__rotator.angle_from_points(face.face_top, face.face_bottom, face.face_left, face.face_right)
            rotation = self.__rotator.new_rotation(angle)
            self.model.rotate(rotation)

    def draw(self):
        self.model.draw()
        