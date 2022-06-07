from circ.thrd import createThread
import client.renderCycle as renderCycle

class worldClass:
    children = []

    def __init__(self):
        self.children = []

    def update(self, dt, events):
        for child in self.children:
            createThread(child.update, dt, events)

worldRoot = worldClass()

renderCycle.addTaskToRenderCycle(worldRoot.update, '_worldUpdate@ONCE')