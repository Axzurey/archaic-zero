import threading
import pygame
import pygame_gui
import client.renderCycle as renderCycle

uiElements = {}

uiManager: pygame_gui.UIManager = None

def startUiCycle():
    global uiManager
    uiManager = pygame_gui.UIManager(renderCycle.localEnv["displayResolution"])

    print('ui manager started')

    def updateUi(dt, events):

        for event in events:
            uiManager.process_events(event)
        
        uiManager.update(dt)

        uiManager.draw_ui(renderCycle.getScreen())

    renderCycle.addTaskToRenderCycle(updateUi, '_uiUpdate')

alreadyInit = False
def initializeUiService():
    global alreadyInit
    if alreadyInit:
        return
    alreadyInit = True

    thr = threading.Thread(target=startUiCycle)
    thr.daemon = True
    thr.start()