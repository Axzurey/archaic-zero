import pygame
import modules.maps as maps
import uuid
from pygame import Rect, Vector2
from modules.quark import switchParent
from circ.thrd import createThread
import modules.mathf as mathf
import gameConstants

from modules.signal import phxSignal
import client.renderCycle as renderCycle
from modules.udim2 import udim2
from worldClass import worldClass

allowsText = {
    'textButton': True,
}

allowsImage = {
    'imageLabel': True,
}

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
        'textColor': '#c5cbd8',
        'borderColor': '#DDDDDD',
        'borderRadius': 10,
        'borderWidth': 5,

        'zindex': 1,

        'mid': 'none',

        'onHoverStart': 'none',
        'onHoverStop': 'none',

        'font': 'fasterOne',
        'fontSize': 10,

        'parent': 'none',
        'children': []
    }

    def __getattr__(self, index):
        if self.properties.get(index) is not None:
            return self.properties[index]
        else:
            return super().__getattribute__(index)

    def __setattr__(self, index, value):
        if self.properties.get(index) is not None:
            if (index == 'parent'):
                switchParent(self, value)
            else:
                self.properties[index] = value
        else:
            super().__setattr__(index, value)
            #raise Exception(f'Property {index} does not exist on this class')
            

    def __init__(self, absoluteType: str):

        self.properties = {
            'absoluteType': 'none', #would be textButton, guiFrame, etc

            'text': '[notext]',
            'size': udim2.fromOffset(200, 150),
            'position': udim2.fromOffset(100, 100),
            'rect': Rect(Vector2(200, 200), Vector2(100, 50)),

            'absolutePosition': Vector2(100, 100),
            'absoluteSize': Vector2(200, 150),

            'backgroundColor': '#45494e',
            'textColor': '#c5cbd8',
            'borderColor': '#DDDDDD',
            'borderRadius': 10,
            'borderWidth': 5,

            'zindex': 1,

            'mid': 'none',

            'onHoverStart': 'none',
            'onHoverStop': 'none',

            'font': 'fasterOne',
            'fontSize': 10,

            'parent': 'none',
            'children': []
        }

        self.absoluteType = absoluteType

        self.mid = str(uuid.uuid4())

        self.onHoverStart = phxSignal()
        self.onHoverStop = phxSignal()

    def subLoad(self, rect, parent):
        self.rect = rect
        if parent:
            self.parent = parent

    def fix(self):
        
        position = None
        size = None
        if self.parent and type(self.parent) != str and type(self.parent) != worldClass:
            pPos = self.parent.absolutePosition
            pSize = self.parent.absoluteSize

            fP = self.position.toScale()
            fpO = self.position.toOffset()
            fS = self.size.toScale()
            fsO = self.size.toOffset()

            position = Vector2(mathf.lerp(pPos.x, pPos.x + pSize.x, fP.x) + fpO.x, mathf.lerp(pPos.y, pPos.y + pSize.y, fP.y) + fpO.y)
            size = Vector2(mathf.lerp(0, pSize.x, fS.x) + fsO.x, mathf.lerp(0, pSize.y, fS.y) + fsO.y)
        
        else:
            container = renderCycle.localEnv["displayResolution"]

            pPos = Vector2(0, 0)
            pSize = Vector2(container[0], container[1])

            fP = self.position.toScale()
            fpO = self.position.toOffset()
            fS = self.size.toScale()
            fsO = self.size.toOffset()

            position = Vector2(mathf.lerp(pPos.x, pPos.x + pSize.x, fP.x) + fpO.x, mathf.lerp(pPos.y, pPos.y + pSize.y, fP.y) + fpO.y)
            size = Vector2(mathf.lerp(0, pSize.x, fS.x) + fsO.x, mathf.lerp(0, pSize.y, fS.y) + fsO.y)
        
        self.absolutePosition = position
        self.absoluteSize = size

        self.rect = pygame.Rect(position, size)

    def update(self, dt, events):

        self.fix()

        screen = renderCycle.getScreen()

        mainS = pygame.Surface(self.absoluteSize)

        mainS.set_alpha((1 - self.transparency) * 255)
        
        main = pygame.draw.rect(screen, self.backgroundColor, self.rect, 0, self.borderRadius if self.borderRadius > 0 else -1)

        border = pygame.draw.rect(screen, self.borderColor, self.rect, self.borderWidth, self.borderRadius if self.borderRadius > 0 else -1)

        #pygame.rect.clip for parent clipping

        if allowsImage.get(self.absoluteType):
                screen.blit(self.image, self.rect)

        if allowsText.get(self.absoluteType):
            b = gameConstants.gameFont.get_rect(self.text)
            sz = Vector2(b.width, b.height)
            gameConstants.gameFont.render_to(screen, (self.absolutePosition + self.absoluteSize / 2) - sz / 2, self.text, self.textColor)

        for child in self.children:
            child.update(dt, events)