import pygame
import uuid
import client.renderCycle as renderCycle
from data.exposed import getSprites

class sprite(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], image: str):

        super().__init__()

        self.rect = pygame.Rect(position, size)
        self.size = size
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)

        self.id = str(uuid.uuid4())

        self.position = pygame.Vector2(position[0], position[1])
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

        self.ignoreCollisionsWith = []

    def setVelocity(self, v: pygame.Vector2) -> None:
        self.velocity = v

    def setAcceleration(self, a: pygame.Vector2):
        self.acceleration = a


    def draw(self):
        print('drawing', self.rect)
        renderCycle.getScreen().blit(self.image, self.rect)

    def getRectPoints(self):
        return (pygame.Vector2(self.rect.topleft), pygame.Vector2(self.rect.topright), pygame.Vector2(self.rect.bottomleft), pygame.Vector2(self.rect.bottomright))

    def checkCollision(self, targetPos: pygame.Vector2, other):
        if pygame.Rect(targetPos, self.size).colliderect(other.rect):
            points0 = self.getRectPoints()
            points1 = other.getRectPoints()

            closestPointsDistance = None
            for point0 in points0:
                for point1 in points1:
                    distance = (point0 - point1).magnitude()

                    if closestPointsDistance == None or distance < closestPointsDistance:
                        closestPointsDistance = distance

            if closestPointsDistance > 1:
                return closestPointsDistance

            return -1
        return 0

    def update(self, allSpriteGroups: dict[str, pygame.sprite.Group]):

        target = self.position + (self.velocity + self.acceleration)

        self.acceleration = pygame.Vector2(0, 0)

        doesPass = True

        for group in allSpriteGroups.values():
            for sprite in group:
                if sprite.id in self.ignoreCollisionsWith or sprite == self:
                    continue

                check = self.checkCollision(target, sprite)
                if check == -1:
                    doesPass = False
                    break
                elif check != 0:
                    dst = self.position - target ##TODO: fix this

                    target = self.position - dst * check
            if not doesPass:
                break

        if doesPass:
            self.position = target
            self.rect = pygame.Rect(self.position, self.size)

        pygame.sprite.Sprite.update(self)

    def delete(self):
        renderCycle.removeTaskFromRenderCycle(self.id)
        pass