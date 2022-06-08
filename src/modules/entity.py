from turtle import pos
import uuid
import pygame
from modules.sprite import sprite
import client.inputService as inputService

class entity:
    def __init__(self, position: tuple[int, int], size: tuple[int, int], image: str):
        self.speed = 600

        self.health = 150
        self.maxHealth = 150

        self.sprite = sprite(position, size, image)

        self.id = str(uuid.uuid4())

    def walkLogic(self, _dt):
        r = inputService.isKeyDown(pygame.K_RIGHT)
        l = inputService.isKeyDown(pygame.K_LEFT)
        u = inputService.isKeyDown(pygame.K_UP)
        d = inputService.isKeyDown(pygame.K_DOWN)
        x = 0
        y = 0
        
        if r:
            x += 1
        elif l:
            x -= 1
        if u:
            y -= 1
        elif d:
            y += 1

        self.sprite.setAcceleration(pygame.Vector2(x, y) * self.speed)

        self.sprite.speed = self.speed

        self.sprite.draw(_dt)