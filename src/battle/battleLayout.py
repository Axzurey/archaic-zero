import random
from circ.thrd import createThread
from components.attackMenu import attackMenu
import battle.battleEntity as battleEntity

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

    def nextTurn():
        global turn
        turn += 1
        print(f'Turn {turn}')
        for movedata in moveQueue:
            movedata['move'](movedata['target'])


        for enemy in enemies:
            enemy.update()
        for teammate in team:
            teammate.update()

        moveQueue.clear()

        #print('NEXT TURN DONE!')

    atkMenu = attackMenu(team, enemies, nextTurn, queueMove)