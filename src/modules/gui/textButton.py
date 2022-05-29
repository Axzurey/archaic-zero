import uuid
from pygame import Rect, Vector2
import pygame_gui
import pygame

import client.uiService as uiService
from modules.signal import phxSignal


class textButton:
    text: str = '[notext]'
    size: Vector2 = Vector2(100, 50)
    position: Vector2 = Vector2(200, 200)
    rect: Rect = Rect(position, size)

    mid = str(uuid.uuid4())

    mouseButton1Click = phxSignal()

    def __init__(self):
        print('instance creating', self.rect, self.size, self.position, self.text)
        self.instance = pygame_gui.elements.UIButton(relative_rect=self.rect, text=self.text, manager=uiService.uiManager)

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

    def update(self, _dt, events):
        for event in events:
            print(event, 'nope')
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                print('it is a press')
                if event.ui_element == self.instance:
                    print('it work')
                    self.mouseButton1Click.emit()