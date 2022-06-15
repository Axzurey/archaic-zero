import random
from struct import calcsize
import time
import pygame
from battle.battleEntity import battleEntity
from circ.thrd import createThread
import client.renderCycle as renderCycle
from game import  createButton, createFrame, createImage, createFloatingTextButton, createPolygon, createScalarBar, createTextLabel
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

tx = 0

class attackMenu():
    def __init__(self, team: list[battleEntity], enemies: list[battleEntity], nextTurn: callable, queueMove: callable):

        self.nextTurn = nextTurn
        self.queueMove = queueMove;

        self.team = team;
        self.enemies = enemies;

        self.currentTarget = self.enemies[0]

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

        enemyBars = []

        attackframes = []

        nextTurnButton = createFloatingTextButton(udim2.fromScale(.2, .8), udim2.fromOffset(100, 100), '>', stasis)

        nextTurnButton.backgroundColor = '#00ff00'

        def updText():
            for dist in enemyBars:
                enemy = dist['enemy']
                bar = dist['bar']
                bar.text = f'{enemy.health} | {enemy.maxHealth}'

                bar.setPercent(enemy.health / enemy.maxHealth)

                

        for enemy in enemies:
            t += 1

            ename = createTextLabel(udim2(320 * t + 50 * t, 0, 0, .04), udim2.fromOffset(300, 35), f'enemy #{t}', stasis)

            ename.backgroundVisible = False
            ename.borderVisible = False

            bar = createScalarBar(udim2(320 * t + 50 * t, 0, -35 / 2, .1), udim2.fromOffset(300, 35), stasis)

            bar.foregroundColor = '#00ff00'
            bar.backgroundColor = '#000000'

            bar.textSize = 10

            bar.text = '250 | 250'

            poly = createPolygon(udim2(320 * t + 50 * t, 0, 0, .1), udim2.fromOffset(0, 0), stasis)

            poly.backgroundColor = typeColors[enemy.type]

            enemy.healthChanged.connect(updText)

            enemyBars.append({
                'bar': bar,
                'poly': poly,
                'ename': ename,
                'enemy': enemy
            })

        moveIndex = 0

        def up(t, v):
            nonlocal moveIndex
            self.queueMove(t, self.currentTarget, v['callback'])
            moveIndex += 1

        for teammate in team:
            attackFrame = createFrame(udim2.fromScale(.64, .73), udim2.fromScale(.35, .25), stasis)

            for x in range(2):
                for y in range(2):
                    v = teammate.moveset[x + y]
                    b = createButton(udim2(10 * x + 280 * x + 10, 0, 10 * y + 110 * y + 10, 0), udim2.fromScale(.4, .3), v["name"], attackFrame)
                    b.backgroundColor = typeColors[v["type"]]

                    b.onMouseClick.connect(lambda: up(teammate, v))

            attackFrame.backgroundColor = '#000000'

            attackframes.append(attackFrame)
            
            attackFrame.visible = False

        updText()

        def run():
            for i in attackframes:
                i.visible = True
                z = moveIndex
                while (z == moveIndex):
                    time.sleep(1 / 60)
                
                i.visible = False
            self.nextTurn()

        nextTurnButton.onMouseClick.connect(run)

        #createThread(self.update)