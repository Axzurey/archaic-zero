import random
import time
from circ.thrd import createThread
from components.attackMenu import attackMenu
import battle.battleEntity as battleEntity

from modules.gui.baseGui import baseGui
from modules.udim2 import udim2
from worldClass import worldRoot
import game

ts = ['water', 'earth', 'air', 'light', 'dark', 'fire']
turn = 0
def createStandardBattle(team: list[battleEntity.battleEntity], enemies: list[battleEntity.battleEntity]):
    from game import INBATTLE, createFrame, createImage, createTextLabel
    global turn
    turn = 1;

    moveQueue = []

    def queueMove(sender: battleEntity, target: battleEntity, move: callable, name: str, t: str):
        moveQueue.append({
            'sender': sender,
            'target': target,
            'move': move,
            'name': name,
            'type': t
        });

    def getNextEnemy():
        for i in range(3):
            enemy = enemies[i]
            if enemy.health > 0:
                return enemy

    def getNextTeamMember():
        for i in range(3):
            member = team[i]
            if member.health > 0:
                return member

    def destroy():
        nonlocal atkMenu

        atkMenu.frames["stasis"].destroy()

    def nextTurn():
        nonlocal atkMenu
        global turn
        nonlocal hitEffect, usedAttackFrame
        turn += 1
        i = 0

        for movedata in moveQueue:

            if getNextEnemy() is None:
                time.sleep(1.5)
                usedAttackText.text = 'No enemies left, you win!'
                usedAttackFrame.visible = True
                time.sleep(1.5)
                game.INBATTLE = False
                destroy()
                break #you win
            if getNextTeamMember() is None:
                time.sleep(1.5)
                usedAttackText.text = 'No teammates left, you lose!'
                usedAttackFrame.visible = True
                time.sleep(1.5)
                game.INBATTLE = False
                game.GAMELOST = True
                destroy()
                break #you lose

            time.sleep(1.5)

            usedAttackFrame.visible = True

            if movedata['type'] == 'you':
                movedata['target'] = getNextEnemy()
                atkMenu.currentTarget = movedata['target']
                atkMenu.setTargetIcons(movedata['target'], False)
            else:
                movedata['target'] = getNextTeamMember()
                atkMenu.currentTeamTarget = movedata['target']
                atkMenu.setTargetIcons(movedata['target'], True)

            if movedata['target'].health <= 0:
                if movedata['type'] == 'you':
                    movedata['target'] = getNextEnemy()
                    atkMenu.currentTarget = movedata['target']
                    atkMenu.setTargetIcons(movedata['target'], False)
                else:
                    movedata['target'] = getNextTeamMember()
                    atkMenu.currentTeamTarget = movedata['target']
                    atkMenu.setTargetIcons(movedata['target'], True)

            hitEffect.visible = True

            if movedata['type'] != 'you':
                t = atkMenu.team.index(movedata['target']) + 1

                hitEffect.position = udim2(90 * t + 260 * t + 140 - 300, 0, 0, .75)
            else:

                t = atkMenu.enemies.index(movedata['target']) + 1

                hitEffect = udim2(320 * t + 50 * t + 140, 0, 0, .25)

            if movedata['sender'].health <= 0:
                i += 1
                print(f'{movedata["sender"].name} is dead, skipping')
                usedAttackFrame.visible = False

                hitEffect.visible = False
                continue

            usedAttackText.text = movedata['sender'].name + ' used ' + movedata['name']

            movedata['move'](movedata['target'])

            time.sleep(1.5)

            usedAttackFrame.visible = False

            hitEffect.visible = False

            i += 1

            if getNextEnemy() is None:
                time.sleep(1.5)
                usedAttackText.text = 'No enemies left, you win!'
                usedAttackFrame.visible = True
                time.sleep(1.5)
                game.INBATTLE = False
                destroy()
                return

            if getNextTeamMember() is None:
                time.sleep(1.5)
                usedAttackText.text = 'No teammates left, you lose!'
                usedAttackFrame.visible = True
                time.sleep(1.5)
                game.INBATTLE = False
                game.GAMELOST = True
                destroy()
                return

        if getNextEnemy() is None:
            time.sleep(1.5)
            usedAttackText.text = 'No enemies left, you win!'
            usedAttackFrame.visible = True
            time.sleep(1.5)
            game.INBATTLE = False
            destroy()
            return

        if getNextTeamMember() is None:
            time.sleep(1.5)
            usedAttackText.text = 'No teammates left, you lose!'
            usedAttackFrame.visible = True
            time.sleep(1.5)
            game.INBATTLE = False
            game.GAMELOST = True
            destroy()
            return

        for enemy in enemies:
            enemy.update()
        for teammate in team:
            teammate.update()

        moveQueue.clear()

    atkMenu = attackMenu(team, enemies, nextTurn, queueMove)

    atkMenu.setTargetIcons(getNextTeamMember(), True)

    atkMenu.setTargetIcons(getNextEnemy(), False)

    usedAttackFrame = createFrame(udim2.fromScale(0, .45), udim2.fromScale(1, .15), atkMenu.frames['stasis'])

    usedAttackFrame.visible = True

    usedAttackText = createTextLabel(udim2.fromOffset(0, 0), udim2.fromScale(1, 1), '', usedAttackFrame)

    usedAttackText.backgroundColor = '#6a6a6a'

    usedAttackText.textColor = '#ffffff'

    usedAttackText.textSize = 75

    usedAttackText.backgroundTransparency = 1
    usedAttackText.borderTransparency = 1

    usedAttackText.text = 'BATTLE STARTED!!!'

    hitEffect = createImage(udim2(0, 0, 0, 0), udim2.fromOffset(100, 100), 'src/images/hit.png')

    hitEffect.visible = False

    time.sleep(1.5)

    atkMenu.frames['stasis'].visible = True

    usedAttackFrame.visible = False

    game.INBATTLE = True
    game.LOADING_BATTLE = False

        #print('NEXT TURN DONE!')