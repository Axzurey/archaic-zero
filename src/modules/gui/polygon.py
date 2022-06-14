import pygame
from modules.gui.baseGui import baseGui
from modules.mathf import pointsOnCircle

class polygon(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('polygon')

        rect = pygame.Rect(100, 100, 100, 100)
        super().subLoad(rect, parent)

        self.properties['vertices'] = pointsOnCircle(40, 6)