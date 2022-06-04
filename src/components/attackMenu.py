import pygame
import client.renderCycle as renderCycle
from game import  createButton, createEntity, createFrame

def createAttackMenu():
    screenX, screenY = renderCycle.getScreen().get_size()

    mainsizeX, mainsizeY = screenX * .33, screenY * .25

    mainpositionX, mainpositionY = screenX * .67, screenY * .75

    attackBar = createFrame(pygame.Vector2(mainpositionX, mainpositionY), pygame.Vector2(mainsizeX, mainsizeY))

    attack1 = createButton(pygame.Vector2(mainsizeX * .05, mainsizeY * .1), pygame.Vector2(mainsizeX * .4, mainsizeY * .3), 'Attack 1', attackBar)

    attack1.backgroundColor = '#BAD6FF'

    attack1.textColor = '#000000'

    attack1.backgroundColorHover = "#00FFFF"

    attack1.shape = 'rounded_rectangle'

    attack1.cornerRadius = 5

    attack1.borderWidth = 2

    attack1.fontSize = 25

    