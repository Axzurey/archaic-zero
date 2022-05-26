import threading
import pygame
from typing import Callable

_tasks: list[Callable[[None], None]] = []

localEnv = {
    "renderFPS": 30
}

def clientClosing() -> bool:
    for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return True
    return False

def addTaskToRenderCycle(task: Callable[[None], None]) -> None:
    _tasks.append(task)

def _renderCycle() -> None:
    clock = pygame.time.Clock()
    while (not clientClosing()):
        clock.tick(localEnv['renderFPS'])


cycleStarted = False

def startCycle() -> None:
    if cycleStarted:
        raise Exception('can not start cycle if cycle already started')
    cycleStarted = True

    thread = threading.Thread(target=_renderCycle)
    thread.daemon = True
    thread.start()