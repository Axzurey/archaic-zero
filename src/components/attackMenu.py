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

        t = 0

        enemyBars = []

        teamBars = []

        attackframes = []

        teamIcons = []

        enemyIcons = []

        self.teamIcons = teamIcons
        self.enemyIcons = enemyIcons

        nextTurnButton = createFloatingTextButton(udim2.fromScale(.92, .9), udim2.fromOffset(100, 100), '>', stasis)

        nextTurnButton.backgroundColor = '#00ff00'

        def updText():
            for dist in enemyBars:
                enemy = dist['enemy']
                bar = dist['bar']
                bar.text = f'{enemy.health} | {enemy.maxHealth}'

                bar.setPercent(enemy.health / enemy.maxHealth)
            for dist in teamBars:
                t = dist['teammate']
                bar = dist['bar']
                bar.text = f'{t.health} | {t.maxHealth}'

                

        for enemy in enemies:
            t += 1

            ename = createTextLabel(udim2(320 * t + 50 * t, 0, 0, .04), udim2.fromOffset(300, 35), f'enemy #{t}', stasis)

            ename.backgroundVisible = False
            ename.borderVisible = False

            icon = createImage(udim2(320 * t + 50 * t + 140, 0, 0, .25), udim2.fromOffset(150, 150), f'src/images/{enemy.type}_phantom.png', stasis)

            icon.backgroundVisible = False
            icon.borderVisible = False

            enemyIcons.append({
                'default': udim2(320 * t + 50 * t + 140, 0, 0, .25),
                'icon': icon,
            })

            bar = createScalarBar(udim2(320 * t + 50 * t, 0, -35 / 2, .1), udim2.fromOffset(300, 35), stasis)

            bar.foregroundColor = '#00ff00'
            bar.backgroundColor = '#000000'

            bar.textColor = '#ffffff'

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

        nxtmv = False

        def up(t, v):
            nonlocal nxtmv
            nonlocal moveIndex
            self.queueMove(t, self.currentTarget, v['callback'])
            moveIndex += 1
            nxtmv = True

        t = 0

        for teammate in team:

            t += 1

            ename = createTextLabel(udim2(90 * t + 260* t - 300, 0, 0, .92), udim2.fromOffset(300 / 1.5, 35 / 1.5), f'teammate #{t}', stasis)

            ename.backgroundVisible = False
            ename.borderVisible = False

            ename.textColor = '#ffffff'

            icon = createImage(udim2(90 * t + 260 * t + 140 - 300, 0, 0, .75), udim2.fromOffset(150 / 1.25, 150 / 1.25), f'src/images/{teammate.type}_phantom.png', stasis)

            icon.backgroundVisible = False
            icon.borderVisible = False

            teamIcons.append({
                'default': udim2(90 * t + 260 * t + 140 - 300, 0, 0, .75),
                'icon': icon,
            })

            bar = createScalarBar(udim2(90 * t + 260 * t - 300, 0, -35 / 1.25 / 2, .9), udim2.fromOffset(300 / 1.25, 35 / 1.25), stasis)

            bar.foregroundColor = '#00ff00'
            bar.backgroundColor = '#000000'

            bar.textColor = '#ffffff'

            bar.textSize = 10

            bar.text = '250 | 250'

            poly = createPolygon(udim2(90 * t + 260 * t - 300, 0, 0, .9), udim2.fromOffset(0, 0), stasis)

            poly.backgroundColor = typeColors[teammate.type]

            teammate.healthChanged.connect(updText)

            attackFrame = createFrame(udim2.fromScale(.69, .73), udim2.fromScale(.3, .25), stasis)

            for x in range(2):
                for y in range(2):
                    v = teammate.moveset[x + y]
                    b = createButton(udim2(10 * x + 240 * x + 10, 0, 10 * y + 110 * y + 10, 0), udim2.fromScale(.4, .3), v["name"], attackFrame)
                    b.backgroundColor = typeColors[v["type"]]

                    b.textColor = '#ffffff'

                    b.onMouseClick.connect(lambda: up(teammate, v))

            attackFrame.backgroundColor = '#000000'

            attackframes.append(attackFrame)
            
            attackFrame.visible = False

        updText()

        def run():
            nonlocal nextTurnButton
            nextTurnButton.visible = False
            time.sleep(.1)
            for i in attackframes:
                i.visible = True
                nonlocal nxtmv
                while (not nxtmv):
                    time.sleep(1 / 60)
                nxtmv = False
                i.visible = False
            self.nextTurn()
            time.sleep(1)
            nextTurnButton.visible = True

        nextTurnButton.onMouseClick.connect(run)

        #createThread(self.update)