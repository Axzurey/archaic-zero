gameEntities: dict[str, any] = {}

def getEntities() -> dict[str, any]:
    return gameEntities

def addEntity(id: str, ent: any) -> None:
    gameEntities[id] = ent

def removeEntity(id: str) -> None:
    gameEntities.pop(id)