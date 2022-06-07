import pygame_gui
from modules.gui.baseGui import baseGui
import client.uiService as uiService
from pygame_gui.core import ObjectID

class guiFrame(baseGui):
    def __init__(self, parent: baseGui = None):
        super().__init__('guiFrame')

        instance = pygame_gui.elements.UIPanel(relative_rect=self.rect, manager=uiService.uiManager, starting_layer_height=1,
        object_id=ObjectID(self.mid, '@button'))
        super().subLoad(instance, parent)