import inspect
import threading
import time
import pygame
from typing import Callable

def createThread(f: callable, *a: any):
    t = threading.Thread(target=f, args=a)
    t.daemon = True
    t.start()
    return t

_tasks: dict[str, Callable[[None], None]] = {}

localEnv = {
    "renderFPS": 60,
    "displayResolution": (1366, 768),
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
def _renderCycle() -> None:
    clock = pygame.time.Clock()

    global clientClosing
    
    while (not clientClosing):

        clock.tick(localEnv['renderFPS'])

        global lastUpdate

        now = time.time()
        dt = now - lastUpdate
        lastUpdate = now

        events = pygame.event.get()

        for ev in events:
            if ev.type == pygame.QUIT:
                clientClosing = True


        for i in list(_tasks):
            task = _tasks[i]

            p = inspect.signature(task).parameters
            p = p.keys()
            if len(p) == 0:
                createThread(task)
            elif len(p) == 1:
                createThread(task, dt)
            elif len(p) == 2:
                createThread(task, dt, events)
            else:
                print('invalid args:', p)
        pygame.display.flip()


cycleStarted = False

def startCycle() -> None:
    global cycleStarted

    if cycleStarted:
        raise Exception('can not start cycle if cycle already started')
        
    cycleStarted = True

    _renderCycle()