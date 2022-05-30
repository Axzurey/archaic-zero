import time
import pygame
import client.renderCycle as renderCycle
import client.uiService as uiService
from game import createButton, createEntity
import game

from modules.themeManager import loadDefaultTheme

pygame.init()

loadDefaultTheme()

res = renderCycle.localEnv['displayResolution']

screen = pygame.display.set_mode(res)

screenCol = (255, 0, 255)

def updateScreen(_dt):
    screen.fill(screenCol)

renderCycle.setScreen(screen)

uiService.initializeUiService()

renderCycle.addTaskToRenderCycle(updateScreen, '_mainUpdate')

time.sleep(1)

player = createEntity(pygame.Vector2(100, 100), pygame.Vector2(50, 50), 'src/images/player_top.png')

button1 = createButton(pygame.Vector2(300, 500), pygame.Vector2(150, 50), 'hello!')

button1.mouseButton1Click.connect(lambda: print('button1 clicked'))

button1.backgroundColor = "#00FFFF"

renderCycle.startCycle()