allStatusses = [
    'burn', #take damage every turn
    'freeze', #will not be able to attack next turn
    'spreadingFire' #next turn, all adjacent enemies will receive this status + burn
]

class battleEntity:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.maxHealth = 100

        self.type = 'fire'

        self.moveset = [
            {
                'name': 'Solar Flare',
                'type': 'fire',
                'callback': lambda target: self.attack(target)
            },
            {
                'name': 'Heat Wave [EX]',
                'type': 'fire',
                'callback': lambda target: target.afflict('burn', 'spreadingFire')
            }
        ]

        self.statusses = []

        self.stats = {
            'critChance': 10,
        }

        self.target = None

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

    def heal(self, heal):
        self.health += heal
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def attack(self, target):
        target.takeDamage(10)

    def afflict(self, *affliction: str):
        for i in [affliction]:
            self.statusses.append(i)