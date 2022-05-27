import pygame
import client.renderCycle as renderCycle
import client.inputService as inputService
from modules.entity import entity
from modules.sprite import sprite

pygame.init()

renderCycle.startCycle()

screen = pygame.display.set_mode((1366, 720))

screenCol = (255, 0, 255)

def updateScreen(_dt):
    screen.fill(screenCol)

renderCycle.setScreen(screen)

renderCycle.addTaskToRenderCycle(updateScreen, '_mainUpdate')

ent = entity()

renderCycle.addTaskToRenderCycle(ent.walkLogic, 'spriteUpd')

while (not renderCycle.clientClosing()):
    pass