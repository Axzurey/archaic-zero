import random
from modules.signal import phxSignal


allStatusses = [
    'burn', #take damage every turn
    'freeze', #will not be able to attack next turn
]

types = ['fire', 'water', 'earth', 'air', 'light', 'dark']

def getMovesFromType(self, type: str):
    moves = {
        'fire': [
            {
                'name': 'Solar Flare',
                'type': 'fire',
                'callback': lambda target: self.attack(target, random.randrange(30, 50))
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
                'name': 'tsunami',
                'type': 'water',
                'callback': lambda target: self.attack(target, random.randrange(25, 40))
            },
            {
                'name': 'waterfall',
                'type': 'water',
                'callback': lambda target: (self.attack(target, random.randrange(30, 50)), target.purgeAfflictions())
            },
        ],
        'earth': [
            {
                'name': 'earthquake',
                'type': 'earth',
                'callback': lambda target: self.attack(target, random.randrange(25, 40))
            },
            {
                'name': 'stone throw',
                'type': 'earth',
                'callback': lambda target: self.attack(target, random.randrange(30, 45))
            },
            {
                'name': 'geo construction',
                'type': 'earth',
                'callback': lambda target: self.attack(target, random.randrange(15, 50))
            }
        ],
        'air': [
            {
                'name': 'wind blast',
                'type': 'air',
                'callback': lambda target: self.attack(target, random.randrange(2, 50))
            },
            {
                'name': 'tornado',
                'type': 'air',
                'callback': lambda target: self.attack(target, random.randrange(25, 75))
            },
            {
                'name': 'wind gust',
                'type': 'air',
                'callback': lambda target: self.attack(target, random.randrange(15, 40))
            }
        ],
        'light': [
            {
                'name': 'lightning bolt',
                'type': 'light',
                'callback': lambda target: self.attack(target, random.randrange(31, 40))
            },
            {
                'name': 'pulsar of light',
                'type': 'light',
                'callback': lambda target: self.attack(target, random.randrange(1, 50, 5))
            },
            {
                'name': 'photon ray',
                'type': 'light',
                'callback': lambda target: self.attack(target, random.randrange(-30, 50))
            },
            {
                'name': 'trick of the light',
                'type': 'light',
                'callback': lambda target: self.attack(target, random.randrange(-25, 75))
            }
        ],
        'dark': [
            {
                'name': 'darkness calling',
                'type': 'dark',

                'callback': lambda target: self.attack(target, random.randrange(30, 50))
            },
            {
                'name': 'Absolute Envelope',
                'type': 'dark',
                'callback': lambda target: self.attack(target, random.randrange(0, 100))
            },
            {
                'name': 'facade',
                'type': 'dark',
                'callback': lambda target: (self.attack(target, random.randrange(0, 50)), self.attack(target, random.randrange(0, 50)), self.attack(target, random.randrange(0, 50)))
            },
            {
                'name': 'nighttime',
                'type': 'dark',
                'callback': lambda target: self.attack(target, random.randrange(1, 55))
            }
        ]
    }

    return moves[type]



class battleEntity:
    def __init__(self, name: str, type: str = None):
        self.name = name
        self.health = 100
        self.maxHealth = 100

        self.type = random.choice(['fire', 'water', 'air', 'earth', 'dark', 'light']) if not type else type

        self.moveset = getMovesFromType(self, self.type)

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