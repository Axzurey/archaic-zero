import modules.maps as maps
import uuid
from pygame import Rect, Vector2
import pygame_gui
from modules.quark import switchParent
import modules.themeManager as themeManager
import modules.mathf as mathf

from modules.signal import phxSignal
import client.renderCycle as renderCycle
from modules.udim2 import udim2

class baseGui:
    properties = {
        'absoluteType': 'none', #would be textButton, guiFrame, etc

        'text': '[notext]',
        'size': udim2.fromOffset(200, 150),
        'position': udim2.fromOffset(100, 100),
        'rect': Rect(Vector2(200, 200), Vector2(100, 50)),

        'absolutePosition': Vector2(100, 100),
        'absoluteSize': Vector2(200, 150),

        'backgroundColor': '#45494e',
        "backgroundColorHover":"#35393e",
        "backgroundColordisabled":"#25292e",
        'textColor': '#c5cbd8',
        "textColorHover":"#FFFFFF",
        "textColorDisabled":"#6d736f",
        'borderColor': '#DDDDDD',
        'borderColorHover': '#FFFFFF',
        'borderColorDisabled': '#808080',

        'zindex': 1,

        'mid': 'none',
        'instance': 'none',

        'mouseButton1Click': 'none',
        'onHoverStart': 'none',
        'onHoverStop': 'none',
        'doubleClick': 'none',

        'font': 'fasterOne',
        'fontSize': 10,

        'shape': 'rounded_rectange', #rectangle, rounded_rectange, ellipse
        'cornerRadius': 10, #only for rounded_rectange
        'borderWidth': 2,
        'shadowWidth': 2,
        'textAlignH': 'center', #left, center, right
        'textAlignV': 'center', #top, center, bottom
    }

    misc = {
        'shape': 'rounded_rectange', #rectangle, rounded_rectange, ellipse
        'shape_corner_radius': '20', #only for rounded_rectange
        'border_width': '2',
        'shadow_width': '2',
        'text_horiz_alignment': 'center', #left, center, right
        'text_vert_alignment': 'center', #top, center, bottom
    }

    font = {
        'name': 'fasterOne',
        'size': 20,
    }

    heiarchy = {
        'children': [],
        'parent': 'none',
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
        elif self.heiarchy.get(index):
            return self.heiarchy[index]

    def __setattr__(self, index, value):
        if maps.colorNameConversion.get(index):
            self.properties[index] = value
            self.colors[maps.colorNameConversion[index]] = value
            themeManager.modifyTheme(self.mid, colorMap=self.colors)
        elif maps.miscNameConversion.get(index):
            value = str(value)
            self.properties[index] = value
            self.misc[maps.miscNameConversion[index]] = value
            themeManager.modifyTheme(self.mid, miscMap=self.misc)
        elif maps.fontNameConversion.get(index):
            self.properties[index] = value
            self.font[maps.fontNameConversion[index]] = value
            themeManager.modifyTheme(self.mid, fontMap=self.font)
        elif self.properties.get(index):
            self.properties[index] = value
        elif self.heiarchy.get(index):
            if (index == 'parent'):
                switchParent(self, value)
            else:
                self.heiarchy[index] = value
        else:
            raise Exception(f'Property {index} does not exist on this class')
            

    def __init__(self, absoluteType: str):

        self.absoluteType = absoluteType

        self.mid = str(uuid.uuid4())

        self.onHoverStart = phxSignal()
        self.onHoverStop = phxSignal()

    def subLoad(self, instance):
        self.instance = instance
        renderCycle.addTaskToRenderCycle(self.update, self.mid + '_update')

    def fix(self):
        position = None
        size = None
        if self.parent and type(self.parent) != str:
            pPos = self.parent.absolutePosition
            pSize = self.parent.absoluteSize

            fP = self.position.toScale()
            fpO = self.position.toOffset()
            fS = self.size.toScale()
            fsO = self.size.toOffset()

            print(self.absoluteType)

            print('btn', pPos, pSize, fP, fpO, fS, fsO)

            position = Vector2(mathf.lerp(pPos.x, pPos.x + pSize.x, fP.x) + fpO.x, mathf.lerp(pPos.y, pPos.y + pSize.y, fP.y) + fpO.y)
            size = Vector2(mathf.lerp(0, pSize.x, fS.x) + fsO.x, mathf.lerp(0, pSize.y, fS.y) + fsO.y)
            self.instance._setup_container(self.parent.instance)
        else:
            container = renderCycle.localEnv["displayResolution"]

            pPos = Vector2(0, 0)
            pSize = Vector2(container[0], container[1])

            fP = self.position.toScale()
            fpO = self.position.toOffset()
            fS = self.size.toScale()
            fsO = self.size.toOffset()

            print('frame', pPos, pSize, fP, fpO, fS, fsO)

            position = Vector2(mathf.lerp(pPos.x, pPos.x + pSize.x, fP.x) + fpO.x, mathf.lerp(pPos.y, pPos.y + pSize.y, fP.y) + fpO.y)
            size = Vector2(mathf.lerp(0, pSize.x, fS.x) + fsO.x, mathf.lerp(0, pSize.y, fS.y) + fsO.y)

        self.absolutePosition = position
        self.absoluteSize = size

        self.instance.set_position(position)
        self.instance.set_dimensions(size)

    def setColors(self):
        self.instance.colours = self.colors

    def update(self, _dt, events):

        self.fix()

        for event in events:
            if hasattr(event, 'ui_element') and event.ui_element == self.instance:
                if event.type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                    self.onHoverStop.emit()
                elif event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
                    self.onHoverStart.emit()