import threading
import pygame
from typing import Callable, Union

_tasks: dict[str, Callable[[None], None]] = {}

localEnv = {
    "renderFPS": 5
}

_screen: pygame.Surface = None

def setScreen(screen):
    global _screen
    _screen = screen

def getScreen():
    return _screen

def clientClosing() -> bool:
    for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return True
    return False

def addTaskToRenderCycle(task: Callable[[None], None], mid: str) -> None:
    _tasks[mid] = task

def removeTaskFromRenderCycle(mid: str) -> None:
    if mid in _tasks:
        del _tasks[mid]


lastUpdate = 0
def _renderCycle() -> None:
    clock = pygame.time.Clock()
    while (not clientClosing()):
        clock.tick(localEnv['renderFPS'])
        for task in _tasks.values():
            task()
        pygame.display.flip()


cycleStarted = False

def startCycle() -> None:
    global cycleStarted

    if cycleStarted:
        raise Exception('can not start cycle if cycle already started')
        
    cycleStarted = True

    thread = threading.Thread(target=_renderCycle)
    thread.daemon = True
    thread.start()