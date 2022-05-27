import pygame
import client.renderCycle as renderCycle
import client.inputService as inputService
from modules.sprite import sprite

pygame.init()

renderCycle.startCycle()
inputService.initializeInputService()

screen = pygame.display.set_mode((1366, 720))

screenCol = (255, 0, 255)

def updateScreen():
    screen.fill(screenCol)

renderCycle.setScreen(screen)

renderCycle.addTaskToRenderCycle(updateScreen, '_mainUpdate')

sp = sprite((100, 100), (100, 100), 'src/images/cookie.png')

while (not renderCycle.clientClosing()):
    pass