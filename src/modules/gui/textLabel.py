import uuid
from pygame import Rect, Vector2
import pygame_gui
import pygame

import client.uiService as uiService
from modules.signal import phxSignal
import client.renderCycle as renderCycle


class textLabel:
    text: str = '[notext]'
    size: Vector2 = Vector2(100, 50)
    position: Vector2 = Vector2(200, 200)
    rect: Rect = Rect(position, size)

    colors = {

    }

    def __init__(self):

        self.mid = str(uuid.uuid4())
        
        self.instance = pygame_gui.elements.UILabel(relative_rect=self.rect, text=self.text, manager=uiService.uiManager, object_id=self.mid)
        renderCycle.addTaskToRenderCycle(self.update, self.mid + '_update')

        self.onHoverStart = phxSignal()
        self.onHoverStop = phxSignal()

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

        self.instance.colours = self.colors

        for event in events:
            if hasattr(event, 'ui_element') and event.ui_element == self.instance:
                if event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                    self.onHoverStop.emit()
                elif event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
                    self.onHoverStart.emit()