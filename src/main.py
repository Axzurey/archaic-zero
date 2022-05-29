import time
import pygame
import client.renderCycle as renderCycle
import client.uiService as uiService
from data.exposed import addEntity
from game import createButton, createEntity
from modules.entity import entity
from modules.gui.textLabel import textLabel
from modules.signal import phxSignal

pygame.init()

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

renderCycle.startCycle()