from object_3d import *
from camera import *
from projection_plane import *
import pygame as pg


class SoftwareRender:
    def __init__ (self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self,[0.5,1,-4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.translate([0.2,0.4,0.2])
        self.axes = Axes(self)
        self.axes.translate([0.7,0.9,0.7])
        self.world_axes = Axes(self)
        self.world_axes.movement_flag = False
        self.world_axes.scale(2.5)
        self.world_axes.translate([0.0001,0.0001,0.0001])

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.world_axes.draw()
        self.axes.draw()
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = SoftwareRender()
    app.run()