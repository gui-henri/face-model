from pyray import *

class Model3D:
    def __init__(self, position: Vector3, model_path: str, texture_path: str = None, scale: float = 1, color: Color = WHITE):
        self.model = load_model(model_path)
        self.texture = load_texture(texture_path)
        self.position = position
        self.scale = scale
        self.color = color
        self.model.materials[0].maps[0].texture = self.texture

    def draw(self):
        draw_model(self.model, self.position, self.scale, self.color)
    
    def rotate(self, angle: Vector3):
        self.model.transform = matrix_rotate_xyz(angle)