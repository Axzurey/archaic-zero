import pygame
from modules.gui.baseGui import baseGui

class imageLabel(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('imageLabel')

        rect = pygame.Rect(100, 100, 100, 100)

        self.properties['image'] = pygame.image.load('src/images/player_top.png')
        self.properties['borderVisible'] = False
        
        super().subLoad(rect, parent)

    def setImage(self, image: str):
        self.properties['image'] = pygame.image.load(image)