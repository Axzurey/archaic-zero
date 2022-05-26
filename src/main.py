import pygame
import client.renderCycle as renderCycle
import client.inputService as inputService

renderCycle.startCycle()
inputService.initializeInputService()

screen = pygame.display.set_mode((1366, 720))

screenCol = (255, 0, 255)
 
posX = 1366 / 2 - 10
 
posY = 720 / 2 - 10
 
circle = pygame.draw.circle(screen, (0, 255, 255), (posX, posY), 10)

def updateScreen():
    screen.fill(screenCol)
    pygame.display.flip()

renderCycle.addTaskToRenderCycle()