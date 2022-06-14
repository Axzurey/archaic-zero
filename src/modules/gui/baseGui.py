import pygame
import pygame.gfxdraw
import numpy
import uuid
from pygame import Rect, Vector2
from modules.quark import switchParent
import modules.mathf as mathf
import gameConstants

from modules.signal import phxSignal
import client.renderCycle as renderCycle
from modules.udim2 import udim2
from worldClass import worldClass

allowsText = {
    'textButton': True,
    'floatingTextButton': True,
    'scalarBar': True,
}

allowsScale = {
    'scalarBar': True,
}

allowsImage = {
    'imageLabel': True,
    #'floatingImageButton': True,
}

allowsShape = {
    'polygon': True,
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

        'shape': 'rect',

        'zindex': 1,

        'visible': True,
        'absoluteVisible': True,

        'mid': 'none',

        'onHoverStart': 'none',
        'onHoverStop': 'none',

        'font': 'fasterOne',
        'fontSize': 10,

        'transparency': 0,
        'borderTransparency': 0,

        'scalePercent': .75,
        'scaleMode': 'linear',

        'foregroundColor': 'A5F488',

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
            elif index == 'fontSize':
                self.localFont = pygame.freetype.Font('src/fonts/Montserrat.ttf', int(value))
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

            'shape': 'rect', #or circle

            'backgroundColor': '#45494e',
            'textColor': '#c5cbd8',
            'borderColor': '#DDDDDD',
            'borderRadius': 10,
            'borderWidth': 5,

            'scalePercent': .75,
            'scaleDelta': 0,
            'targetPercent': .75,
            'scaleMode': 'linear',
            'scaleLength': 1, #in seconds

            'hovering': False,

            'foregroundColor': 'A5F488',

            'transparency': 0,
            'borderTransparency': 0,

            'zindex': 1,

            'visible': True,
            'absoluteVisible': True,

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
        self.onMouseClick = phxSignal()

        self.mouseDown = False;
        self.localFont = pygame.freetype.Font('src/fonts/Montserrat.ttf', 20)

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

        if self.visible and (type(self.parent) == worldClass or self.parent.visible):

            self.absoluteVisible = True;

            screen = renderCycle.getScreen()
            if allowsShape.get(self.absoluteType) is not None:
                if len(self.vertices) > 2:
                    p = []
                    for v in self.vertices:
                        p.append(v + self.absolutePosition)
                    poly = pygame.draw.polygon(screen, self.backgroundColor, p, 0)
                    border = pygame.draw.polygon(screen, self.borderColor, p, self.borderWidth)
            elif allowsScale.get(self.absoluteType) is not None:
                t = self.scaleDelta / self.scaleLength
                if self.scaleMode == 'linear':

                    t = round(t, 3)
                    self.scalePercent = mathf.lerp(self.scalePercent, self.targetPercent, t)

                    self.scaleDelta = numpy.clip(self.scaleDelta + dt, 0, self.scaleLength)

                shadow = pygame.Surface(self.rect.size, pygame.SRCALPHA)
                shadow.fill((0, 0, 0, 255 * .1))
                screen.blit(shadow, self.absolutePosition + Vector2(0, 5))

                back = pygame.draw.rect(screen, self.backgroundColor, self.rect, 0, self.borderRadius if self.borderRadius > 0 else -1)

                scaledRect = pygame.Rect(self.absolutePosition, Vector2(self.scalePercent * self.absoluteSize.x, self.absoluteSize.y))

                front = pygame.draw.rect(screen, self.foregroundColor, scaledRect, 0, self.borderRadius if self.borderRadius > 0 else -1)
            else:
                if self.shape == 'rect':


                    main = pygame.draw.rect(screen, self.backgroundColor, self.rect, 0, self.borderRadius if self.borderRadius > 0 else -1)

                    border = pygame.draw.rect(screen, self.borderColor, self.rect, self.borderWidth, self.borderRadius if self.borderRadius > 0 else -1)
                
                elif self.shape == 'circle':

                    dropShadow = pygame.draw.circle(screen, (13, 13, 13), self.absolutePosition - Vector2(0, -4), self.absoluteSize.x / 2, 0)
                    
                    main = pygame.draw.circle(screen, self.backgroundColor, self.absolutePosition, self.absoluteSize.x / 2, 0)

            if allowsImage.get(self.absoluteType):
                
                self.image = pygame.transform.scale(self.image, self.absoluteSize.xx / 1.25)
                r = self.image.get_rect()
                r = r.move(self.absolutePosition - self.absoluteSize / 2)
                screen.blit(self.image, r)

            if allowsText.get(self.absoluteType):
                if self.shape == 'rect':
                    b = self.localFont.get_rect(self.text)
                    sz = Vector2(b.width, b.height)
                    self.localFont.render_to(screen, (self.absolutePosition + self.absoluteSize / 2) - sz / 2, self.text, self.textColor)
                elif self.shape == 'circle':
                    self.localFont.size = 80
                    b = self.localFont.get_rect(self.text)
                    sz = Vector2(b.width, b.height)
                    self.localFont.render_to(screen, self.absolutePosition - sz / 2, self.text, self.textColor)
        
        else:
            self.absoluteVisible = False;

        if pygame.mouse.get_pressed()[0]:
            if not self.mouseDown and self.rect.collidepoint(pygame.mouse.get_pos()):
                self.onMouseClick.emit()
        else:
            self.mouseDown = False;

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovering:
                self.hovering = True
                self.onHoverStart.emit()
        else:
            if self.hovering:
                self.hovering = False
                self.onHoverStop.emit()

        for child in self.children:
            child.update(dt, events)