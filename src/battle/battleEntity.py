import random
from modules.signal import phxSignal


allStatusses = [
    'burn', #take damage every turn
    'freeze', #will not be able to attack next turn
]

types = ['fire', 'water', 'earth', 'air', 'light', 'dark']

def getRandomMovesFromType(self, type: str):
    moves = {
        'fire': [
            {
                'name': 'Solar Flare',
                'type': 'fire',
                'callback': lambda target: self.attack(target, random.randrange(30, 50))
            },
            {
                'name': 'Heat Wave [EX]',
                'type': 'fire',
                'callback': lambda target: (target.afflict({
                    'type': 'burn',
                    'duration': 3,
                    'callback': lambda: self.takeDamage(random.randrange(10, 20)),
                    'tick': 0
                }), self.attack(target, random.randrange(10, 30)))
            },
            {
                'name': 'volcanic eruption',
                'type': 'fire',
                'callback': lambda target: (target.afflict({
                    'type': 'burn',
                    'duration': 3,
                    'callback': lambda: self.takeDamage(random.randrange(10, 20)),
                    'tick': 0
                }), self.attack(target, random.randrange(10, 30)))
            },
            {
                'name': 'fireball',
                'type': 'fire',
                'callback': lambda target: self.attack(target, random.randrange(25, 50))
            },
            {
                'name': 'flame burst',
                'type': 'fire',
                'callback': lambda target: self.attack(target, random.randrange(30, 45))
            }
        ],
        'water': [
            {
                'name': 'water blast',
                'type': 'water',
                'callback': lambda target: self.attack(target, random.randrange(30, 50))
            },
            {
                'name': 'water wave',
                'type': 'water',
                'callback': lambda target: self.attack(target, random.randrange(30, 50))
            },
            {
                'name': 'obliteration',
                'type': 'water',
                'callback': lambda target: self.attack(target, random.randrange(300, 1550))
            },
            {
                'name': 'tsunami',
                'type': 'water',
                'callback': lambda target: self.attack(target, random.randrange(25, 40))
            },
            {
                'name': 'waterfall',
                'type': 'water',
                'callback': lambda target: (self.attack(target, random.randrange(30, 50)), target.purgeAfflictions())
            },
            {
                'name': 'rainy day',
                'type': 'water',
                'callback': lambda target: (self.purgeAfflictions(), self.afflict({
                    'type': 'regeneration',
                    'duration': 3,
                    'callback': lambda: self.heal(random.randrange(15, 30)),
                    'tick': 0
                }))
            }
        ]
    }

    return [random.choice(moves[type]) for _ in range(4)]



class battleEntity:
    def __init__(self, name: str):
        self.name = name
        self.health = 300
        self.maxHealth = 300

        self.type = random.choice(['fire', 'water'])

        self.moveset = getRandomMovesFromType(self, self.type)

        self.statusses = []

        self.stats = {
            'critChance': 10,
        }

        self.target = None

        self.healthChanged = phxSignal()

    def update(self):
        for i in self.statusses:
            if i['tick'] > i['duration']:
                self.statusses.remove(i)
                continue
        
            i['callback']()

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

    def purgeAfflictions(self):
        self.statusses.clear()

    def attack(self, target, damage):
        target.takeDamage(damage)

    def afflict(self, *affliction: str):
        for i in affliction:
            self.statusses.append(i)