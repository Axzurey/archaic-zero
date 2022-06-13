import random
from struct import calcsize
import time
import pygame
from circ.thrd import createThread
import client.renderCycle as renderCycle
from game import  createButton, createFrame, createImage, createFloatingTextButton, createScalarBar
from modules.udim2 import udim2
from worldClass import worldRoot

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

        bar = createScalarBar(udim2.fromScale(.2, .2), udim2.fromOffset(400, 100), stasis)

        bar.foregroundColor = '#00ff00'
        bar.backgroundColor = '#000000'

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