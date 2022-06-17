from modules.entity import entity
import pygame
import client.inputService as inputService

class enemyEntity(entity):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], image: str):
        super().__init__(position, size, image)
