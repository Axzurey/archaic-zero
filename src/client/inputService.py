import threading
import pygame

from client.renderCycle import clientClosing



def inputLoop() -> None:
    while not clientClosing():
        print(pygame.key.get_pressed())


_inputServiceInitialized = False
def initializeInputService() -> None:
    if (_inputServiceInitialized): return
    _inputServiceInitialized = True

    thread = threading.Thread(target=inputLoop)
    thread.daemon = True
    thread.start()