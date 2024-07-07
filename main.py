from sys import argv

import face_detection as fd
from sprite import Sprite
import webcam as wc
from raylib_app import RayLibApp
from rat_face import RatFace

def main(tshirt_path, background_path, webcam_index):
    face_detection = fd.FaceLandmarkDetection()
    webcam = wc.WebCam(webcam_index)
    app = RayLibApp(1280, 720, "Leptospiroserson", 30)

    rat_face = RatFace(webcam, face_detection)
    app.entities_3d.append(rat_face)

    tshirt = Sprite((285, 325), tshirt_path, scale=1.3)
    background = Sprite((0, -200), background_path, scale=1.2)
    app.sprites.append(background)
    app.sprites.append(tshirt)

    app.run()
    
    webcam.release()
    app.end()

def get_args():
    webcam_index = 0
    if len(argv) > 1:
        webcam_index = int(argv[1])
    background_path = "data/cavaleiro.jpg"
    if len(argv) > 2:
        background_path = argv[2]
    tshirt_path = "data/img.png"
    if len(argv) > 3:
        tshirt_path = argv[3]
    return webcam_index, background_path, tshirt_path

if __name__ == "__main__":
    webcam_index, background_path, tshirt_path = get_args()
    main(tshirt_path, background_path, webcam_index)
