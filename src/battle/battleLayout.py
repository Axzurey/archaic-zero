import random
from components.attackMenu import attackMenu
import battle.battleEntity as battleEntity

ts = ['water', 'earth', 'air', 'light', 'dark', 'fire']

def createStandardBattle():
    turn = 1;

    enemies = []
    team = []

    for i in range(3):
        enemy = battleEntity.battleEntity(f'enemy{i}')
        enemies.append(enemy)
        enemy.type = random.choice(ts)
    
    for i in range(3):
        member = battleEntity.battleEntity(f'member{i}')
        team.append(member)

    atkMenu = attackMenu(team, enemies)