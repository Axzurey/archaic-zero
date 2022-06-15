import time
import pygame
from battle.battleLayout import createStandardBattle
import client.renderCycle as renderCycle
from definedWorld import loadWorld
from game import createPlayer
from modules.themeManager import loadDefaultTheme

pygame.init()

loadDefaultTheme()

res = renderCycle.localEnv['displayResolution']

screen = pygame.display.set_mode(res)

renderCycle.setScreen(screen)

time.sleep(1)

loadWorld()

#player = createPlayer(pygame.Vector2(0, 0), pygame.Vector2(50, 50), 'src/images/player_top.png')

#player.speed = 20

createStandardBattle()

renderCycle.startCycle()