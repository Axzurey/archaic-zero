from pygame import Rect, Vector2
import pygame_gui

import client.uiService as uiService


class textLabel:
    text: str = '[notext]'
    size: Vector2 = Vector2(100, 50)
    position: Vector2 = Vector2(200, 200)
    rect: Rect = Rect(position, size)
    def __init__(self):
        print('instance creating', self.rect, self.size, self.position, self.text)
        self.instance = pygame_gui.elements.UILabel(relative_rect=self.rect, text=self.text, manager=uiService.uiManager)

    def setText(self, text):
        self.text = text
        self.fix()

    def setPosition(self, position):
        self.position = position
        self.rect = Rect(self.position, self.size)
        self.fix()

    def setSize(self, size):
        self.size = size
        self.rect = Rect(self.position, self.size)
        self.fix()

    def fix(self):
        self.instance.set_position(self.position)
        self.instance.set_dimensions(self.size)
        self.instance.set_text(self.text)

    def update(self):
        self.instance.set_position(self.position)
        self.instance.set_dimensions(self.size)
        self.instance.set_text(self.text)