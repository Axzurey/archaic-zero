import threading

from pygame import Vector2

def fromUdim(offsetX: float = 0, scaleX: float = 0, offsetY: float = 0, scaleY: float = 0):
    def calculate(max: Vector2):
        maxX = max.x
        maxY = max.y

        return Vector2(maxX * scaleX + offsetX, maxY * scaleY + offsetY)

    return {
        "calculate": calculate
    }

def switchParent(c, p):
    print('switch start', c, p)
    px = c.parent

    if c == p:
        raise Exception('Cannot set parent to self')

    if px and type(px) != str:
        if px.children.count(c) > 0:
            px.children.remove(c)
    
    p.heiarchy['children'].append(c)
    c.heiarchy['parent'] = p

def createThread(f: callable, *a: any):
    t = threading.Thread(target=f, args=a)
    t.daemon = True
    t.start()
    return t