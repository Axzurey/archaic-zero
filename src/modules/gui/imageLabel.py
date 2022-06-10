import pygame
from modules.gui.baseGui import baseGui

class imageLabel(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('imageLabel')

        rect = pygame.Rect(100, 100, 100, 100)
        super().subLoad(rect, parent)

        self.properties['image'] = pygame.image.load('src/images/player_top.png')

    def setImage(self, image: str):
        self.properties['image'] = pygame.image.load(image)