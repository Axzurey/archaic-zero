import pygame
import modules.sprite as sprite
import client.inputService as inputService

class entity:
    def __init__(self):
        self.speed = 100

        self.health = 150
        self.maxHealth = 150

        self.sprite = sprite((100, 100), (100, 100), 'src/images/cookie.png')

    def walkLogic(self, _dt):
        r = inputService.isKeyDown(pygame.K_RIGHT)
        l = inputService.isKeyDown(pygame.K_LEFT)
        u = inputService.isKeyDown(pygame.K_UP)
        d = inputService.isKeyDown(pygame.K_DOWN)
        x = 0
        y = 0
        
        if r:
            x += 50
        elif l:
            x -= 50
        if u:
            y -= 50
        elif d:
            y += 50

        self.sprite.setAcceleration = pygame.Vector2(x, y)
        self.sprite.draw(_dt)