import pygame
from modules.gui.baseGui import baseGui

class guiFrame(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('guiFrame')

        rect = pygame.Rect(100, 100, 250, 100)
        super().subLoad(rect, parent)