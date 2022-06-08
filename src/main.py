import time
import pygame
import client.renderCycle as renderCycle
import client.uiService as uiService
from components.attackMenu import createAttackMenu
from definedWorld import loadWorld
from game import createEntity
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

loadWorld()

player = createEntity(pygame.Vector2(0, 0), pygame.Vector2(50, 50), 'src/images/player_top.png')

player.speed = 120

createAttackMenu()

renderCycle.startCycle()