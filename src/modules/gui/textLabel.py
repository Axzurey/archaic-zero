import pygame
from modules.gui.baseGui import baseGui

class textLabel(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('textLabel')

        rect = pygame.Rect(100, 100, 300, 100)
        super().subLoad(rect, parent)

    def setText(self, text: str):
        self.text = text