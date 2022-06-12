from components.attackMenu import attackMenu
import battle.battleEntity as battleEntity

def createStandardBattle():
    turn = 1;

    enemies = []
    team = []

    for i in range(3):
        enemy = battleEntity.battleEntity(f'enemy{i}')
        enemies.append(enemy)
    
    for i in range(3):
        member = battleEntity.battleEntity(f'member{i}')
        team.append(member)

    atkMenu = attackMenu(team, enemies)