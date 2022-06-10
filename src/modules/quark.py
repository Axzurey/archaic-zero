from worldClass import worldRoot

def switchParent(c, p):
    px = c.parent

    if c == p:
        raise Exception('Cannot set parent to self')

    if px and type(px) != str:
        if px.children.count(c) > 0:
            px.children.remove(c)

    if p == worldRoot:
        c.properties["parent"] = worldRoot
        worldRoot.children.append(c)
    else:
        p.properties['children'].append(c)
        c.properties['parent'] = p