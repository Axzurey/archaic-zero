import pygame
from client.renderCycle import clientClosing

def isKeyDown(key: int) -> bool:
    keys = pygame.key.get_pressed()
    if keys[key]: return True
    return False