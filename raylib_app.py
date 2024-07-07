from sprite import Sprite
from pyray import *

class RayLibApp:
    def __init__(self, width, height, title, fps):
        self.width = width
        self.height = height
        self.title = title
        self.fps = fps
        self.camera = Camera3D((0, 2.6, 3.2), (0, 2, 0), (0, 1, 0), 60)
        self.background_color = GREEN
        self.sprites: list[Sprite] = []
        self.entities_3d = []

        init_window(self.width, self.height, self.title)
        set_target_fps(self.fps)
        disable_cursor()

    def run(self):
        while not window_should_close():
            self.update()
            self.draw()

    def update(self):
        for entitiy in self.entities_3d:
            entitiy.update()

    def draw(self):
        begin_drawing()
        clear_background(self.background_color)
        for sprite in self.sprites:
            sprite.draw()
        begin_mode_3d(self.camera)
        for entity in self.entities_3d:
            entity.draw()
        end_mode_3d()
        end_drawing()

    def end(self):
        close_window()
