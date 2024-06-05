import pygame as pg
import numpy as np
from camera import *
from obj3d import *
from projection import *

WHITE = (255, 255, 255)
BLACK = (0,0,0)

class Rendering:

    def __init__(self):
        pg.init()
        self.SCREEN_W, self.SCREEN_H = 1200, 800
        self.screen = pg.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.surf = pg.surface.Surface((self.SCREEN_W, self.SCREEN_H))
        self.fps = 60
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = obj3d(self)

        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi / 3)

        self.world_axes = Axes(self)
        self.world_axes.scale(2.5)
        self.world_axes.translate((0.0001, 0.0001, 0.0001))

    def draw(self):
        self.screen.fill(BLACK)
        self.world_axes.draw()
        self.object.draw()

    def run(self):
        running = True
        while running:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.camera.control()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)



if __name__ == "__main__":
    app = Rendering()
    app.run()


