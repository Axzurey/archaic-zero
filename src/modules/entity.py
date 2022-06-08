import uuid
from modules.sprite import sprite
import client.inputService as inputService

class entity:
    def __init__(self, position: tuple[int, int], size: tuple[int, int], image: str):
        self.speed = 600

        self.health = 150
        self.maxHealth = 150

        self.sprite = sprite(position, size, image)

        self.id = str(uuid.uuid4())