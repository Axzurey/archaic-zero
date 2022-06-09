import pygame
from modules.gui.baseGui import baseGui

class textButton(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('textButton')

        rect = pygame.Rect(100, 100, 250, 100)
        super().subLoad(rect, parent)

    def setText(self, text: str):
        self.text = text

        