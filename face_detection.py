import mediapipe as mp

class Face:
    def __init__(self, face_landmarks):
        self.face_left = face_landmarks[127]
        self.face_right = face_landmarks[356]
        self.face_top = face_landmarks[10]
        self.face_bottom = face_landmarks[152]

class FaceLandmarkDetection:
    def __init__(self):
        self.__mp_face_mesh = mp.solutions.face_mesh
        self.__face_mesh = self.__mp_face_mesh.FaceMesh()
    def process(self, frame):
        results = self.__face_mesh.process(frame)
        if results.multi_face_landmarks:
            return Face(results.multi_face_landmarks[0].landmark)
        else:
            return None