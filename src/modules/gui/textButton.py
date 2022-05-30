import modules.maps as maps
import uuid
from pygame import Rect, Vector2
import pygame_gui
from pygame_gui.core import ObjectID
import modules.themeManager as themeManager

import client.uiService as uiService
from modules.signal import phxSignal
import client.renderCycle as renderCycle


class textButton:
    
    properties = {
        'text': '[notext]',
        'size': Vector2(100, 50),
        'position': Vector2(200, 200),
        'rect': Rect(Vector2(200, 200), Vector2(100, 50)),

        'backgroundColor': '#45494e',
        "backgroundColorHover":"#35393e",
        "backgroundColordisabled":"#25292e",
        'textColor': '#c5cbd8',
        "textColorHover":"#FFFFFF",
        "textColorDisabled":"#6d736f",
        'borderColor': '#DDDDDD',
        'borderColorHover': '#FFFFFF',
        'borderColorDisabled': '#808080',

        'mid': 'none',
        'instance': 'none',

        'mouseButton1Click': 'none',
        'onHoverStart': 'none',
        'onHoverStop': 'none',
        'doubleClick': 'none',
    }

    colors = {
        "normal_bg":"#45494e",
        "hovered_bg":"#35393e",
        "disabled_bg":"#25292e",
        "selected_bg":"#193754",
        "dark_bg":"#15191e",
        "normal_text":"#c5cbd8",
        "hovered_text":"#FFFFFF",
        "selected_text":"#FFFFFF",
        "disabled_text":"#6d736f",
        "link_text": "#0000EE",
        "link_hover": "#2020FF",
        "link_selected": "#551A8B",
        "text_shadow": "#777777",
        "normal_border": "#DDDDDD",
        "hovered_border": "#B0B0B0",
        "disabled_border": "#808080",
        "selected_border": "#8080B0",
        "active_border": "#8080B0",
        "filled_bar":"#f4251b",
        "unfilled_bar":"#CCCCCC"
    }

    def __getattr__(self, index):
        if (maps.colorNameConversion.get(index)):
            return self.colors[maps.colorNameConversionInverse[index]]
        elif self.properties.get(index):
            return self.properties[index]

    def __setattr__(self, index, value):
        if maps.colorNameConversion.get(index):
            self.properties[index] = value
            self.colors[maps.colorNameConversion[index]] = value
            themeManager.modifyThemeColors(self.mid, self.colors)
        elif self.properties.get(index):
            self.properties[index] = value
        else:
            raise Exception(f'Property {index} does not exist on this class')
            

    def __init__(self):

        self.mid = str(uuid.uuid4())
        
        self.instance = pygame_gui.elements.UIButton(relative_rect=self.rect, text=self.text, manager=uiService.uiManager, 
        object_id=ObjectID(self.mid, '@button'))
        renderCycle.addTaskToRenderCycle(self.update, self.mid + '_update')

        self.mouseButton1Click = phxSignal()
        self.onHoverStart = phxSignal()
        self.onHoverStop = phxSignal()
        self.doubleClick = phxSignal()

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

        self.fix()

        for event in events:
            if hasattr(event, 'ui_element') and event.ui_element == self.instance:
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    self.mouseButton1Click.emit()
                elif event.type == pygame_gui.UI_BUTTON_DOUBLE_CLICKED:
                    self.doubleClick.emit()
                elif event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                    self.onHoverStop.emit()
                elif event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
                    self.onHoverStart.emit()