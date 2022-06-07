import pygame_gui
from modules.gui.baseGui import baseGui
import client.uiService as uiService
from pygame_gui.core import ObjectID

class textButton(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('textButton')

        instance = pygame_gui.elements.UIButton(relative_rect=self.rect, manager=uiService.uiManager, text=self.text,
        object_id=ObjectID(self.mid, '@button'))
        super().subLoad(instance, parent)

    def setText(self, text: str):
        self.text = text

        