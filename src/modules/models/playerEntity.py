from modules.entity import entity
import pygame
import client.inputService as inputService

class playerEntity(entity):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], image: str):
        super().__init__(position, size, image)

    def update(self):

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
