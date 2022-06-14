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
        enemy.type = random.choice(ts)
        enemy.afflict('burn')
    
    for i in range(3):
        member = battleEntity.battleEntity(f'member{i}')
        team.append(member)

    def nextTurn():
        global turn
        turn += 1
        print(f'Turn {turn}')
        for i in enemies:
            i.update()
        for i in team:
            i.update()

    atkMenu = attackMenu(team, enemies, nextTurn)