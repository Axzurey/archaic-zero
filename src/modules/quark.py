import threading

def switchParent(c, p):
    print('switch start', c, p)
    px = c.parent

    if c == p:
        raise Exception('Cannot set parent to self')

    if px and type(px) != str:
        px.children.remove(c)
    
    p.heiarchy['children'].append(c)
    c.heiarchy['parent'] = p

def createThread(f: callable, *a: any):
    t = threading.Thread(target=f, args=a)
    t.daemon = True
    t.start()
    return t