import pygame
from modules.gui.baseGui import baseGui

class scalarBar(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('scalarBar')

        rect = pygame.Rect(100, 100, 300, 100)
        super().subLoad(rect, parent)

    def setPercent(self, percent: float):
        self.scalePercent = percent;

    def setText(self, text: str):
        self.text = text