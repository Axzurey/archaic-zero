gameEntities: dict[str, any] = {}
gameSprites: dict[str, any] = {}

def getEntities() -> dict[str, any]:
    return gameEntities

def getSprites() -> dict[str, any]:
    return gameSprites

def addEntity(id: str, ent: any) -> None:
    gameEntities[id] = ent

def addSprite(id: str, ent: any) -> None:
    gameSprites[id] = ent

def removeSprite(id: str) -> None:
    gameSprites.pop(id)

def removeEntity(id: str) -> None:
    gameEntities.pop(id)