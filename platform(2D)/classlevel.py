import pygame
from config import *

class level:
    def __init__(self, displaysurface):
        self.dispaysurface = displaysurface
        
    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        self.update()
        self.draw()