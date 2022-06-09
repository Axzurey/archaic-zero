from circ.thrd import createThread

class worldClass:
    children = []

    def __init__(self):
        self.children = []

    def update(self, dt, events):
        for child in self.children:
            child.update(dt, events)

worldRoot = worldClass()