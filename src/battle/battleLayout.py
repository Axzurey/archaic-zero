import random
import time
from circ.thrd import createThread
from components.attackMenu import attackMenu
import battle.battleEntity as battleEntity
from modules.gui.baseGui import baseGui

ts = ['water', 'earth', 'air', 'light', 'dark', 'fire']
turn = 0
def createStandardBattle():
    global turn
    turn = 1;

    enemies = []
    team = []

    for i in range(3):
        enemy = battleEntity.battleEntity(f'enemy{i}')
        enemies.append(enemy)
    
    for i in range(3):
        member = battleEntity.battleEntity(f'member{i}')
        team.append(member)

    moveQueue = []

    def queueMove(sender: battleEntity, target: battleEntity, move):
        moveQueue.append({
            'sender': sender,
            'target': target,
            'move': move
        });

    atkMenu = attackMenu(team, enemies, nextTurn, queueMove)


    def nextTurn():
        nonlocal atkMenu
        global turn
        turn += 1
        print(f'Turn {turn}')
        i = 0
        for movedata in moveQueue:
            movedata['move'](movedata['target'])
            
            z: baseGui = atkMenu.teamIcons[i] if i < 3 else atkMenu.enemyIcons[i - 3]

            i += 1


        for enemy in enemies:
            enemy.update()
        for teammate in team:
            teammate.update()

        moveQueue.clear()

        #print('NEXT TURN DONE!')