import inspect
import time
import pygame
from typing import Callable
from circ.thrd import createThread

_tasks: dict[str, Callable[[None], None]] = {}

localEnv = {
    "renderFPS": 60,
    "displayResolution": (1500, 800),
}

_screen: pygame.Surface = None

def setScreen(screen):
    global _screen
    _screen = screen

def getScreen():
    return _screen

def addTaskToRenderCycle(task: Callable[[None], None], mid: str) -> None:
    _tasks[mid] = task

def removeTaskFromRenderCycle(mid: str) -> None:
    if mid in _tasks:
        del _tasks[mid]

clientClosing = False
lastUpdate = 0

lastEvents = []

def _renderCycle() -> None:
    clock = pygame.time.Clock()

    global clientClosing
    
    while (not clientClosing):

        global lastUpdate

        now = time.time()
        dt = now - lastUpdate
        lastUpdate = now

        events = pygame.event.get()

        lastEvents = events

        for ev in events:
            if ev.type == pygame.QUIT:
                clientClosing = True


        for i in list(_tasks):
            task = _tasks[i]
            p = inspect.signature(task).parameters
            p = p.keys()
            if len(p) == 0:
                task()
            elif len(p) == 1:
                task(dt)
            elif len(p) == 2:
                task(dt, events)
            else:
                print('invalid args:', p)
        #pygame.display.flip()

        clock.tick(localEnv['renderFPS'])


cycleStarted = False

def startCycle() -> None:
    global cycleStarted

    if cycleStarted:
        raise Exception('can not start cycle if cycle already started')
        
    cycleStarted = True

    _renderCycle()