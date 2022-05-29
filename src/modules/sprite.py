import pygame
import uuid
import client.renderCycle as renderCycle
from data.exposed import getEntities

class sprite:
    def __init__(self, position: tuple[int, int], size: tuple[int, int], image: str):
        self.rect = pygame.Rect(position, size)
        self.size = size
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)

        self.id = str(uuid.uuid4())

        self.position = pygame.Vector2(position[0], position[1])
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

        renderCycle.addTaskToRenderCycle(self.draw, self.id)

    def checkCollision(self, other: any):
        return self.rect.colliderect(other.rect)

    def checkNextCollision(self, nextPos, other: any):
        return pygame.Rect(nextPos, self.size).colliderect(other.rect)

    def setVelocity(self, v: pygame.Vector2) -> None:
        self.velocity = v

    def setAcceleration(self, a: pygame.Vector2):
        self.acceleration = a

    def draw(self, dt: float):
        
        target = self.position + (self.velocity + self.acceleration) * dt

        self.acceleration = pygame.Vector2()

        entities = getEntities()

        p = True

        for x in list(entities):
            e = entities[x]
            if e.sprite == self:
                continue
            if self.checkNextCollision(target, e.sprite):
                p = False
                break

        if p:
            self.position = target
            self.rect = pygame.Rect(self.position, self.size)

        renderCycle.getScreen().blit(self.image, self.rect)

    def delete(self):
        renderCycle.removeTaskFromRenderCycle(self.id)
        pass