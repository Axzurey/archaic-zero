import pygame
import uuid
import client.renderCycle as renderCycle
from data.exposed import getSprites

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

        self.ignoreCollisionsWith = []

        renderCycle.addTaskToRenderCycle(self.draw, self.id)

    def checkCollision(self, other: any):
        return self.rect.colliderect(other.rect)

    def checkNextCollision(self, nextPos, other: any):
        return pygame.Rect(nextPos, self.size).colliderect(other.rect)

    def getPartial(self, nextPos, other):
        if pygame.Rect(pygame.Vector2(self.position.x, nextPos.y), self.size).colliderect(other.rect) and pygame.Rect(pygame.Vector2(nextPos.x, self.position.y), self.size).colliderect(other.rect):
            return None
        else:
            if pygame.Rect(pygame.Vector2(nextPos.x, self.position.y), self.size).colliderect(other.rect):
                return pygame.Vector2(self.position.x, nextPos.y)
            elif pygame.Rect(pygame.Vector2(self.position.x, nextPos.y), self.size).colliderect(other.rect):
                return pygame.Vector2(nextPos.x, self.position.y)
            else:
                return nextPos

    def setVelocity(self, v: pygame.Vector2) -> None:
        self.velocity = v

    def setAcceleration(self, a: pygame.Vector2):
        self.acceleration = a

    def draw(self, dt: float):
        
        target = self.position + (self.velocity + self.acceleration) * dt

        self.acceleration = pygame.Vector2(0, 0)

        entities = getSprites()

        p = True

        closestOne = None

        for x in list(entities):
            e = entities[x]
            if e == self or self.ignoreCollisionsWith.count(e) > 0:
                continue
            if self.checkNextCollision(target, e):
                z = self.getPartial(target, e)

                if not z:

                    break #will collide, just ignore

                p = False
                """
                if closestOne:
                    if (z - target).magnitude() < (closestOne - target).magnitude():
                        closestOne = z
                else:
                    closestOne = z"""
        if p:
            self.position = target
        elif closestOne:
            self.position = closestOne
            
        self.rect = pygame.Rect(self.position, self.size)
        renderCycle.getScreen().blit(self.image, self.rect)

    def delete(self):
        renderCycle.removeTaskFromRenderCycle(self.id)
        pass