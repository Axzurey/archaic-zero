import pygame
from modules.gui.baseGui import baseGui

class floatingTextButton(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('floatingTextButton')

        rect = pygame.Rect(100, 100, 100, 100)
        super().subLoad(rect, parent)

        self.properties['image'] = pygame.image.load('src/images/player_top.png')

        self.properties['borderRadius'] = 90

        self.properties['shape'] = 'circle'

        self.properties['text'] = 'X'

    def setImage(self, image: str):
        self.properties['image'] = pygame.image.load(image)

    def setText(self, text: str):
        self.text = text