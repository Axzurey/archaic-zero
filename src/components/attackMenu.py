import random
from struct import calcsize
import time
import pygame
from circ.thrd import createThread
import client.renderCycle as renderCycle
from game import  createButton, createFrame, createImage, createFloatingTextButton, createPolygon, createScalarBar
from modules.udim2 import udim2
from worldClass import worldRoot

typeColors = {
    'fire': '#ff0000',
    'water': '#0000ff',
    'earth': '#00ff00',
    'air': '#ffff00',
    'light': '#ff00ff',
    'dark': '#00ffff',
}

class attackMenu():
    def __init__(self, team, enemies):

        self.team = team;
        self.enemies = enemies;

        self.frames = {
            "stasis": None
        }

        self.frames["stasis"] = createFrame(udim2.fromOffset(0, 0), udim2.fromScale(1, 1), worldRoot)

        stasis = self.frames["stasis"]

        #stasis.transparency = 1;
        #stasis.borderTransparency = 1;

        attackButton = createFloatingTextButton(udim2.fromScale(.8, .8), udim2.fromOffset(100, 100), 'A', stasis)

        attackButton.backgroundColor = '#888585'

        attackButton.borderWidth = 2

        attackButton.borderRadius = 90

        t = 0

        for enemy in enemies:
            t += 1

            bar = createScalarBar(udim2(0, .16 * t + .1 * t, -35 / 2, .2), udim2.fromOffset(300, 35), stasis)

            bar.foregroundColor = '#00ff00'
            bar.backgroundColor = '#000000'

            bar.textSize = 10

            bar.text = '250 | 250'

            poly = createPolygon(udim2.fromScale(.15 * t + .1 * t, .2), udim2.fromOffset(0, 0), stasis)

            poly.backgroundColor = typeColors[enemy.type]

        def ud():
            time.sleep(3)
            bar.setPercent(.5)
            time.sleep(3)
            bar.setPercent(.75)
            time.sleep(3)
            bar.setPercent(1)
            time.sleep(3)
            bar.setPercent(0)
            time.sleep(3)
            bar.setPercent(1)

        createThread(ud)

    def update(self):
        pass