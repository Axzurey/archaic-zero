from struct import calcsize
import pygame
import client.renderCycle as renderCycle
from game import  createButton, createEntity, createFrame
from modules.quark import fromUdim

def createAttackMenu():
    screenX, screenY = renderCycle.getScreen().get_size()

    mainsizeX, mainsizeY = screenX * .33, screenY * .25

    mainpositionX, mainpositionY = screenX * .67, screenY * .75

    attackBar = createFrame(pygame.Vector2(mainpositionX, mainpositionY), pygame.Vector2(mainsizeX, mainsizeY))

    for x in range(1, 3):
        for y in range(1, 3):
            udSize = fromUdim(scaleX=.4, scaleY=.2)
            calcSize = udSize["calculate"](attackBar.size)

            udPos = fromUdim(scaleX=.25 * x, scaleY=.25 * y)
            calcPos = udPos["calculate"](attackBar.position - attackBar.size)

            print(calcSize, calcPos)

            attack1 = createButton(calcPos, calcSize, f'Attack {x + y}', attackBar)

            attack1.backgroundColor = '#BAD6FF'

            attack1.textColor = '#000000'

            attack1.backgroundColorHover = "#00FFFF"

            attack1.shape = 'rounded_rectangle'

            attack1.cornerRadius = 5

            attack1.borderWidth = 2

            attack1.fontSize = 25

    

    