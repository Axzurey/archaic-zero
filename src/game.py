import time
from typing import Union
from pygame import Vector2
import pygame
import client.renderCycle as renderCycle
from data.exposed import addEntity, addSprite
from modules.entity import entity
from modules.gui.floatingTextButton import floatingTextButton
from modules.gui.textLabel import textLabel
from modules.gui.polygon import polygon
from modules.gui.scalarBar import scalarBar
from modules.gui.guiFrame import guiFrame
from modules.gui.textButton import textButton
from modules.gui.imageLabel import imageLabel
from modules.models.playerEntity import playerEntity
from modules.sprite import sprite
from modules.udim2 import udim2
from worldClass import worldClass, worldRoot

spriteGroups = {
    'worldModel': pygame.sprite.Group(),
    'character': pygame.sprite.Group(),
    'otherEntities': pygame.sprite.Group()
}

updatableUI = {

}

entities: dict[str, entity] = {}

sprites: dict[str, sprite] = {}

lastupd = time.time()

INBATTLE = False

GAMELOST = True

def drawAllSpriteGroups():

    global lastupd

    dt = time.time() - lastupd

    for v in spriteGroups.values():
        v.update(spriteGroups)

    screenCol = (255, 0, 255)
    screen = renderCycle.getScreen()

    screen.fill(screenCol)

    for v in spriteGroups.values():
        v.draw(renderCycle.getScreen())


    worldRoot.update(dt, renderCycle.lastEvents)

    lastupd = time.time()

    pygame.display.update()

renderCycle.addTaskToRenderCycle(drawAllSpriteGroups, 'process:drawAllSpriteGroups')

def createPlayer(position: Vector2, size: Vector2, imagePath: str):
    plr = playerEntity(position, size, imagePath)

    addEntity(plr.id, plr)

    entities[plr.id] = plr

    spriteGroups['character'].add(plr.sprite)

    renderCycle.addTaskToRenderCycle(plr.update, f'{plr.id}:update')

    return plr

def createEntity(position: Vector2, size: Vector2, imagePath: str):
    ent = entity(position, size, imagePath)

    addEntity(ent.id, ent)

    entities[ent.id] = ent

    spriteGroups['otherEntities'].add(ent.sprite)

    return ent

def createSprite(position: Vector2, size: Vector2, imagePath: str) -> sprite:
    s = sprite(position, size, imagePath)
    sprites[s.id] = s

    addSprite(s.id, s)

    #renderCycle.addTaskToRenderCycle(s.draw, f'{s.id}:draw')
    return s

def createTextLabel(position: udim2, size: udim2, text: str, parent: guiFrame = None) -> textLabel:
    t = textLabel(parent)
    t.position = position
    t.size = size
    t.setText(text)

    updatableUI[t.mid] = t
    return t

def createScalarBar(position: udim2, size: udim2, parent: guiFrame = None) -> scalarBar:
    t = scalarBar(parent)
    t.position = position
    t.size = size

    updatableUI[t.mid] = t
    return t

def createPolygon(position: udim2, size: udim2, parent: guiFrame = None) -> polygon:
    t = polygon(parent)
    t.position = position
    t.size = size

    updatableUI[t.mid] = t
    return t

def createFloatingTextButton(position: udim2, size: udim2, text: str, parent: guiFrame = None) -> textButton:
    t = floatingTextButton(parent)
    t.position = position
    t.size = size
    t.setText(text)

    updatableUI[t.mid] = t
    return t

def createFrame(position: udim2, size: udim2, parent: Union[guiFrame, worldClass] = None) -> guiFrame:
    t = guiFrame(parent)
    t.position = position
    t.size = size

    updatableUI[t.mid] = t
    return t

def createImage(position: udim2, size: udim2, imagePath: str, parent: guiFrame = None) -> imageLabel:
    t = imageLabel(parent)
    t.position = position
    t.size = size
    t.setImage(imagePath)

    updatableUI[t.mid] = t

    return t

def createButton(position: udim2, size: udim2, text: str, parent: guiFrame = None) -> textButton:
    t = textButton(parent)
    t.position = position
    t.size = size
    t.setText(text)

    updatableUI[t.mid] = t
    return t