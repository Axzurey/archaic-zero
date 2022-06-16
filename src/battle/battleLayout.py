import random
import time
from circ.thrd import createThread
from components.attackMenu import attackMenu
import battle.battleEntity as battleEntity
from game import createFrame, createTextLabel
from modules.gui.baseGui import baseGui
from modules.udim2 import udim2
from worldClass import worldRoot

ts = ['water', 'earth', 'air', 'light', 'dark', 'fire']
turn = 0
def createStandardBattle():
    global turn
    turn = 1;

    enemies = []
    team = []

    for i in range(3):
        enemy = battleEntity.battleEntity(f'enemy #{i}')
        enemies.append(enemy)
    
    for i in range(3):
        member = battleEntity.battleEntity(f'teammate #{i}')
        team.append(member)

    moveQueue = []

    def queueMove(sender: battleEntity, target: battleEntity, move: callable, name: str):
        moveQueue.append({
            'sender': sender,
            'target': target,
            'move': move,
            'name': name
        });

    def nextTurn():
        nonlocal atkMenu
        global turn
        turn += 1
        print(f'Turn {turn}')
        i = 0
        for movedata in moveQueue:

            usedAttackFrame.visible = True

            usedAttackText.text = movedata['sender'].name + ' used ' + movedata['name']

            time.sleep(2)

            movedata['move'](movedata['target'])

            usedAttackFrame.visible = False

            i += 1

        for enemy in enemies:
            enemy.update()
        for teammate in team:
            teammate.update()

        moveQueue.clear()

    atkMenu = attackMenu(team, enemies, nextTurn, queueMove)

    usedAttackFrame = createFrame(udim2.fromScale(0, .4), udim2.fromScale(1, .2), worldRoot)

    usedAttackFrame.visible = False

    usedAttackText = createTextLabel(udim2.fromOffset(0, 0), udim2.fromScale(1, 1), '', usedAttackFrame)

    usedAttackText.backgroundColor = '#6a6a6a'

    usedAttackText.textColor = '#ffffff'

    usedAttackText.textSize = 75

    usedAttackText.backgroundTransparency = 1
    usedAttackText.borderTransparency = 1

        #print('NEXT TURN DONE!')