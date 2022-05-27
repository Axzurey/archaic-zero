import threading
import pygame

from client.renderCycle import clientClosing



def inputLoop() -> None:
    while not clientClosing():
        pass

_inputServiceInitialized = False
def initializeInputService() -> None:
    global _inputServiceInitialized
    if (_inputServiceInitialized): return
    _inputServiceInitialized = True

    thread = threading.Thread(target=inputLoop)
    thread.daemon = True
    thread.start()