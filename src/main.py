import time
import pygame
import client.renderCycle as renderCycle
import client.uiService as uiService
from game import createButton, createEntity, createFrame
from modules.quark import createThread
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

player = createEntity(pygame.Vector2(0, 0), pygame.Vector2(50, 50), 'src/images/player_top.png')

frame1 = createFrame(pygame.Vector2(100, 100), pygame.Vector2(1000, 600))

button1 = createButton(pygame.Vector2(120, 120), pygame.Vector2(150, 50), 'hello!', frame1)

button1.mouseButton1Click.connect(lambda: print('button1 clicked'))

button1.backgroundColor = "#45494e"

button1.backgroundColorHover = "#00FFFF"

button1.shape = 'rounded_rectangle'

button1.cornerRadius = 5

button1.borderWidth = 2

button1.fontSize = 30

#button1.position = pygame.Vector2(0, 0)

#button1.parent = frame1

print(button1.parent, button1.children)

print(frame1.parent, frame1.children)

renderCycle.startCycle()