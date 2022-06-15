import random
from modules.signal import phxSignal


allStatusses = [
    'burn', #take damage every turn
    'freeze', #will not be able to attack next turn
    'spreadingFire' #next turn, all adjacent enemies will receive this status + burn
]

types = ['fire', 'water', 'earth', 'air', 'light', 'dark']

def getRandomMovesFromType(self, type: str):
    moves = {
        'fire': [
            {
                'name': 'Solar Flare',
                'type': 'fire',
                'callback': lambda target: self.attack(target, 50)
            },
            {
                'name': 'Heat Wave [EX]',
                'type': 'fire',
                'callback': lambda target: (target.afflict('burn', 'spreadingFire'), self.attack(target, 30))
            },
            {
                'name': 'volcanic eruption',
                'type': 'fire',
                'callback': lambda target: (target.afflict('burn', 'spreadingFire'), self.attack(target, 30))
            },
            {
                'name': 'fireball',
                'type': 'fire',
                'callback': lambda target: self.attack(target, 40)
            },
        ]
    }

    return [random.choice(moves[type]) for _ in range(4)]



class battleEntity:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.maxHealth = 100

        self.type = random.choice(types)

        self.moveset = getRandomMovesFromType(self, self.type)

        self.statusses = []

        self.stats = {
            'critChance': 10,
        }

        self.target = None

        self.healthChanged = phxSignal()

    def update(self):
        for i in self.statusses:
            if i == 'burn':
                self.takeDamage(1)
            if i == 'freeze':
                self.takeDamage(1)
            if i == 'spreadingFire':
                self.takeDamage(1)

    def setTarget(self, target):
        self.target = target

    def useMove(self, moveName):
        if self.target:
            self.moveset[moveName]['callback'](self, self.target)
        else:
            print('no target!')

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0 #it dead now
        self.healthChanged.emit()

    def heal(self, heal):
        self.health += heal
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def attack(self, target, damage):
        target.takeDamage(damage)

    def afflict(self, *affliction: str):
        for i in affliction:
            self.statusses.append(i)